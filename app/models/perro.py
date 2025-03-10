from flask_login import UserMixin
from app.config.db import db

class Perro(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=True)
    raza = db.Column(db.String(20), nullable=True)
    edad = db.Column(db.Integer, nullable=True)
    