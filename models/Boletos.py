from sqlalchemy import ForeignKey
from db import db


class Boletos(db.Model):
    __tablename__ = "boletos"

    id = db.Column(db.Integer, primary_key=True)
    asiento_pasajero = db.Column(db.Integer, db.ForeignKey("asientos.id"))
    id_pasajero = db.Column(db.Integer, db.ForeignKey("pasajeros.id"))
    id_autobus = db.Column(db.Integer, db.ForeignKey("autobuses.id"))
    id_viaje = db.Column(db.Integer, db.ForeignKey("viajes.id"))
    fecha_compra = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    precio = db.Column(db.DECIMAL(10, 2))
    estatus_pago = db.Column(db.Enum('Pagado', 'Pendiente'))
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    ultima_actualizacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), server_onupdate=db.func.current_timestamp())

