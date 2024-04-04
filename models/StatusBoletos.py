from sqlalchemy import ForeignKey
from db import db


class StatusBoletos(db.Model):
    __tablename__ = "status_boletos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
