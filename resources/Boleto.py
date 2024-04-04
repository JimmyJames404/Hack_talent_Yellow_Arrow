from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import Boletos, Asientos, Pasajeros, Autobuses, Viajes
from schemas import BoletoSchema

blp = Blueprint("boletos", "boletos", description="Operaciones en boletos")


@blp.route("/boleto/<int:boleto_id>")
class Boleto(MethodView):
    @blp.response(200, BoletoSchema)
    def get(self, boleto_id):
        boleto = Boletos.query.get_or_404(boleto_id)
        return boleto

    def delete(self, boleto_id):
        boleto = Boletos.query.get_or_404(boleto_id)
        db.session.delete(boleto)
        db.session.commit()
        return {"mensaje": "Boleto eliminado"}


@blp.route("/boleto")
class ListaBoletos(MethodView):
    @blp.response(200, BoletoSchema(many=True))
    def get(self):
        boletos = Boletos.query.all()
        return boletos

    @blp.arguments(BoletoSchema)
    @blp.response(201, BoletoSchema)
    def post(self, boleto_data):
        asiento_pasajero_id = boleto_data.pop("asiento_pasajero_id")
        id_pasajero = boleto_data.pop("id_pasajero")
        id_autobus = boleto_data.pop("id_autobus")
        id_viaje = boleto_data.pop("id_viaje")

        asiento_pasajero = Asientos.query.get_or_404(asiento_pasajero_id)
        pasajero = Pasajeros.query.get_or_404(id_pasajero)
        autobus = Autobuses.query.get_or_404(id_autobus)
        viaje = Viajes.query.get_or_404(id_viaje)

        boleto = Boletos(
            asiento_pasajero=asiento_pasajero,
            pasajero=pasajero,
            autobus=autobus,
            viaje=viaje,
            **boleto_data
        )

        try:
            db.session.add(boleto)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return boleto
