import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import Estacion
from schemas import EstacionSchema

blp = Blueprint("estaciones", __name__, description="Operaciones en estaciones")


@blp.route("/estacion/<int:estacion_id>")
class Estacion(MethodView):
    @blp.response(200, EstacionSchema)
    def get(self, estacion_id):
        estacion = Estacion.query.get_or_404(estacion_id)
        return estacion

    def delete(self, estacion_id):
        estacion = Estacion.query.get_or_404(estacion_id)
        db.session.delete(estacion)
        db.session.commit()
        return {"mensaje": "Estación eliminada"}


@blp.route("/estacion")
class ListaDeEstaciones(MethodView):
    @blp.response(200, EstacionSchema(many=True))
    def get(self):
        return Estacion.query.all()

    @blp.arguments(EstacionSchema)
    @blp.response(200, EstacionSchema)
    def post(self, estacion_data):
        estacion = Estacion(**estacion_data)
        try:
            db.session.add(estacion)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Ya existe una estación con ese nombre.")
        except SQLAlchemyError:
            abort(500, message="Ocurrió un error al crear la estación.")

        return estacion
