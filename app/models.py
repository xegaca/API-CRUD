from app import db
from sqlalchemy.orm import validates


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    @validates("name")  # SQLAlchemy usa este decorador para validar "name".
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        return value

    def __repr__(self):
        return f"<Data id={self.id} name={self.name}>"
