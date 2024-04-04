from sqlalchemy import ForeignKey
from db import db


class Choferes(db.Model):
    __tablename__ = "choferes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    licencia_conducir = db.Column(db.String(20))
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    ultima_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), server_onupdate=db.func.current_timestamp())

