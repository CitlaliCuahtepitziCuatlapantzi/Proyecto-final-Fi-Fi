from . import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Persona(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    email=db.Column(db.String(100))
    password_hash=db.Column(db.String(100))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_active(self):
        return True

    def eliminar_usuario(self):
        db.session.delete(self)
        db.session.commit()