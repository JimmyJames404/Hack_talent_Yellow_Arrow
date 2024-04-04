import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import Paradas
from schemas import ParadaSchema

blp = Blueprint("paradas", __name__, description="Operaciones en paradas")


@blp.route("/parada/<int:parada_id>")
class Parada(MethodView):
    @blp.response(200, ParadaSchema)
    def get(self, parada_id):
        parada = Paradas.query.get_or_404(parada_id)
        return parada

    def delete(self, parada_id):
        parada = Paradas.query.get_or_404(parada_id)
        db.session.delete(parada)
        db.session.commit()
        return {"mensaje": "Parada eliminada"}


@blp.route("/parada")
class ListaParadas(MethodView):
    @blp.response(200, ParadaSchema(many=True))
    def get(self):
        return Paradas.query.all()

    @blp.arguments(ParadaSchema)
    @blp.response(201, ParadaSchema)
    def post(self, parada_data):
        parada = Paradas(**parada_data)
        try:
            db.session.add(parada)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Ocurrió un error al crear la parada.")

        return parada
