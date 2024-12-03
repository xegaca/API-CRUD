import pytest
from app import create_app, db
from app.models import Data

# Configuración inicial para pruebas
@pytest.fixture
def app():
    # Crear la aplicación de prueba con configuración de pruebas
    app = create_app("testing")

    # Contexto para la base de datos
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    # Cliente de pruebas
    return app.test_client()


# Pruebas para la ruta POST /data
def test_insert_data(client):
    response = client.post("/data", json={"name": "Test Name"})
    assert response.status_code == 200
    assert response.json == {"message": "Data inserted successfully"}

    # Intentar insertar un duplicado
    response_duplicate = client.post("/data", json={"name": "Test Name"})
    assert response_duplicate.status_code == 409
    assert response_duplicate.json == {"message": "Data already exists"}


# Pruebas para la ruta GET /data
def test_get_all_data(client):
    # Insertar datos iniciales
    db.session.add(Data(name="Test 1"))
    db.session.add(Data(name="Test 2"))
    db.session.commit()

    response = client.get("/data")
    assert response.status_code == 200

    data = response.json
    assert len(data) == 2
    assert data[0]["name"] == "Test 1"
    assert data[1]["name"] == "Test 2"


# Pruebas para la ruta DELETE /data/<id>
def test_delete_data(client):
    # Insertar un dato inicial
    new_data = Data(name="To Delete")
    db.session.add(new_data)
    db.session.commit()

    # Verificar que el dato existe
    data_id = new_data.id
    response = client.get("/data")
    assert any(item["id"] == data_id for item in response.json)

    # Eliminar el dato
    response_delete = client.delete(f"/data/{data_id}")
    assert response_delete.status_code == 200
    assert response_delete.json == {"message": "Data deleted successfully"}

    # Verificar que el dato ya no existe
    response_after_delete = client.get("/data")
    assert not any(item["id"] == data_id for item in response_after_delete.json)

    # Intentar eliminar un dato inexistente
    response_delete_missing = client.delete(f"/data/{data_id}")
    assert response_delete_missing.status_code == 404
    assert response_delete_missing.json == {"message": "Data not found"}
