from sqlalchemy import ForeignKey
from db import db

class Pasajeros(db.Model):
    __tablename__ = "pasajeros"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer)
    fecha_nacimiento = db.Column(db.DATE)
    curp = db.Column(db.String(18))
    correo_electronico = db.Column(db.String(255))
    numero_telefonico = db.Column(db.String(15))
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    ultima_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), server_onupdate=db.func.current_timestamp())

