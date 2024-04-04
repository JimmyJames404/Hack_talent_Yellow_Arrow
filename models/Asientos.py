from sqlalchemy import ForeignKey
from db import db


class Asientos(db.Model):
    __tablename__ = "asientos"

    id = db.Column(db.Integer, primary_key=True)
    asiento = db.Column(db.String(10), nullable=False)
    formacion_autobus = db.Column(db.Integer, db.ForeignKey("autobuses.id"))
    tipo_asiento = db.Column(db.Enum('Ventana', 'Pasillo'))
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    ultima_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), server_onupdate=db.func.current_timestamp())

