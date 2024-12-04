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

# Test para la creación del modelo
def test_create_data(new_data):
    assert new_data.id is not None
    assert new_data.name == "Test Model"

# Test para el método __repr__ del modelo
def test_repr(new_data):
    repr_str = repr(new_data)
    assert repr_str == f"<Data id={new_data.id} name={new_data.name}>"
