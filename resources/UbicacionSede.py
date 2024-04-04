import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import UbicacionesSede
from schemas import UbicacionSedeSchema

blp = Blueprint("ubicaciones_sede", __name__, description="Operaciones en ubicaciones de sede")


@blp.route("/ubicacion_sede/<int:ubicacion_id>")
class UbicacionSede(MethodView):
    @blp.response(200, UbicacionSedeSchema)
    def get(self, ubicacion_id):
        ubicacion = UbicacionesSede.query.get_or_404(ubicacion_id)
        return ubicacion

    def delete(self, ubicacion_id):
        ubicacion = UbicacionesSede.query.get_or_404(ubicacion_id)
        db.session.delete(ubicacion)
        db.session.commit()
        return {"mensaje": "Ubicación de sede eliminada"}


@blp.route("/ubicacion_sede")
class ListaUbicacionesSede(MethodView):
    @blp.response(200, UbicacionSedeSchema(many=True))
    def get(self):
        return UbicacionesSede.query.all()

    @blp.arguments(UbicacionSedeSchema)
    @blp.response(201, UbicacionSedeSchema)
    def post(self, ubicacion_data):
        ubicacion = UbicacionesSede(**ubicacion_data)
        try:
            db.session.add(ubicacion)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Ocurrió un error al crear la ubicación de sede.")

        return ubicacion
