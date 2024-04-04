from sqlalchemy import ForeignKey
from db import db


class Estacion(db.Model):
    __tablename__ = "estacion"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    latitud = db.Column(db.DECIMAL(9, 6))
    longitud = db.Column(db.DECIMAL(9, 6))
    direccion = db.Column(db.String(255))
    telefonos = db.Column(db.String(255))
    capacidad = db.Column(db.Integer)
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    ultima_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), server_onupdate=db.func.current_timestamp())
