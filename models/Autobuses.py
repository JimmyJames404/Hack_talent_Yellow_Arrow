from sqlalchemy import ForeignKey
from db import db


class Autobuses(db.Model):
    __tablename__ = "autobuses"

    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100))
    ubicacion_actual = db.Column(db.Integer, db.ForeignKey("estacion.id"))
    capacidad = db.Column(db.Integer)
    asientos_disponibles = db.Column(db.Integer)
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    ultima_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), server_onupdate=db.func.current_timestamp())

