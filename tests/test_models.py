import pytest
from app import create_app, db
from app.models import Data


# Configuración de la base de datos para pruebas
@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def new_data(app):
    data = Data(name="Test Model")
    with app.app_context():
        db.session.add(data)
        db.session.commit()
    return data


def test_create_data(app):
    with app.app_context():
        new_data = Data(name="Test Model")
        db.session.add(new_data)
        db.session.commit()

        # Refresca manualmente la instancia para evitar DetachedInstanceError
        db.session.refresh(new_data)

        assert new_data.id is not None
        assert new_data.name == "Test Model"


def test_repr(app):
    with app.app_context():
        new_data = Data(name="Repr Test")
        db.session.add(new_data)
        db.session.commit()

        # Refresca manualmente la instancia para evitar DetachedInstanceError
        db.session.refresh(new_data)

        repr_str = repr(new_data)
        assert repr_str == f"<Data id={new_data.id} name={new_data.name}>"


# Test para crear datos con nombre vacío
def test_create_data_with_empty_name(app):
    with app.app_context():
        with pytest.raises(ValueError, match="Name cannot be empty"):
            new_data = Data(name="")
            db.session.add(new_data)
            db.session.commit()


# Test para consultar datos
def test_query_data(app):
    data1 = Data(name="Query Test 1")
    data2 = Data(name="Query Test 2")
    db.session.add(data1)
    db.session.add(data2)
    db.session.commit()

    retrieved_data = Data.query.all()
    assert len(retrieved_data) == 2
    assert retrieved_data[0].name == "Query Test 1"
    assert retrieved_data[1].name == "Query Test 2"


# Test para eliminar datos
def test_delete_data(app):
    with app.app_context():
        data = Data(name="To Delete")
        db.session.add(data)
        db.session.commit()

        retrieved_data = db.session.get(Data, data.id)
        assert retrieved_data is not None

        db.session.delete(retrieved_data)
        db.session.commit()

        assert db.session.get(Data, data.id) is None


# Test para actualizar datos
def test_update_data(app):
    data = Data(name="Update Test")
    db.session.add(data)
    db.session.commit()

    # Actualizar el nombre
    data.name = "Updated Name"
    db.session.commit()

    updated_data = Data.query.get(data.id)
    assert updated_data.name == "Updated Name"


# Test para nombres duplicados
def test_duplicate_name(app):
    with app.app_context():
        data1 = Data(name="Duplicate Test")
        db.session.add(data1)
        db.session.commit()

        with pytest.raises(Exception):
            data2 = Data(name="Duplicate Test")
            db.session.add(data2)
            db.session.commit()
