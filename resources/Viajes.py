import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import Viajes, Estacion
from schemas import ViajeSchema

blp = Blueprint("viajes", __name__, description="Operaciones en viajes")


@blp.route("/viaje/<int:viaje_id>")
class Viaje(MethodView):
    @blp.response(200, ViajeSchema)
    def get(self, viaje_id):
        viaje = Viajes.query.get_or_404(viaje_id)
        return viaje

    def delete(self, viaje_id):
        viaje = Viajes.query.get_or_404(viaje_id)
        db.session.delete(viaje)
        db.session.commit()
        return {"mensaje": "Viaje eliminado"}


@blp.route("/viaje")
class ListaDeViajes(MethodView):
    @blp.response(200, ViajeSchema(many=True))
    def get(self):
        return Viajes.query.all()

    @blp.arguments(ViajeSchema)
    @blp.response(201, ViajeSchema)
    def post(self, viaje_data):
        origen_id = viaje_data.pop("origen_id")
        destino_id = viaje_data.pop("destino_id")

        origen = Estacion.query.get_or_404(origen_id)
        destino = Estacion.query.get_or_404(destino_id)

        viaje = Viajes(origen=origen, destino=destino, **viaje_data)

        try:
            db.session.add(viaje)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Ocurrió un error al crear el viaje.")

        return viaje
