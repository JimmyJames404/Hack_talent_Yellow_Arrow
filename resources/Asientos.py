from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import Asientos, Autobuses
from schemas import AsientoSchema

blp = Blueprint("asientos", "asientos", description="Operaciones en asientos")


@blp.route("/asiento/<int:asiento_id>")
class Asiento(MethodView):
    @blp.response(200, AsientoSchema)
    def get(self, asiento_id):
        asiento = Asientos.query.get_or_404(asiento_id)
        return asiento

    def delete(self, asiento_id):
        asiento = Asientos.query.get_or_404(asiento_id)
        db.session.delete(asiento)
        db.session.commit()
        return {"mensaje": "Asiento eliminado"}


@blp.route("/asiento")
class ListaAsientos(MethodView):
    @blp.response(200, AsientoSchema(many=True))
    def get(self):
        asientos = Asientos.query.all()
        return asientos

    @blp.arguments(AsientoSchema)
    @blp.response(201, AsientoSchema)
    def post(self, asiento_data):
        formacion_autobus_id = asiento_data.pop("formacion_autobus_id")
        formacion_autobus = Autobuses.query.get_or_404(formacion_autobus_id)

        asiento = Asientos(formacion_autobus=formacion_autobus, **asiento_data)

        try:
            db.session.add(asiento)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return asiento
