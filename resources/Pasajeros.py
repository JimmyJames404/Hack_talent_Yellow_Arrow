from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import Pasajeros
from schemas import PasajeroSchema

blp = Blueprint("pasajeros", "pasajeros", description="Operaciones en pasajeros")


@blp.route("/pasajero/<int:pasajero_id>")
class Pasajero(MethodView):
    @blp.response(200, PasajeroSchema)
    def get(self, pasajero_id):
        pasajero = Pasajeros.query.get_or_404(pasajero_id)
        return pasajero

    def delete(self, pasajero_id):
        pasajero = Pasajeros.query.get_or_404(pasajero_id)
        db.session.delete(pasajero)
        db.session.commit()
        return {"mensaje": "Pasajero eliminado"}


@blp.route("/pasajero")
class ListaPasajeros(MethodView):
    @blp.response(200, PasajeroSchema(many=True))
    def get(self):
        pasajeros = Pasajeros.query.all()
        return pasajeros

    @blp.arguments(PasajeroSchema)
    @blp.response(201, PasajeroSchema)
    def post(self, pasajero_data):
        pasajero = Pasajeros(**pasajero_data)

        try:
            db.session.add(pasajero)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return pasajero
