from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import Autobuses, Estacion
from schemas import AutobusSchema

blp = Blueprint("autobuses", "autobuses", description="Operaciones en autobuses")


@blp.route("/autobus/<int:autobus_id>")
class Autobus(MethodView):
    @blp.response(200, AutobusSchema)
    def get(self, autobus_id):
        autobus = Autobuses.query.get_or_404(autobus_id)
        return autobus

    def delete(self, autobus_id):
        autobus = Autobuses.query.get_or_404(autobus_id)
        db.session.delete(autobus)
        db.session.commit()
        return {"mensaje": "Autobús eliminado"}


@blp.route("/autobus")
class ListaAutobuses(MethodView):
    @blp.response(200, AutobusSchema(many=True))
    def get(self):
        autobuses = Autobuses.query.all()
        return autobuses

    @blp.arguments(AutobusSchema)
    @blp.response(201, AutobusSchema)
    def post(self, autobus_data):
        ubicacion_actual_id = autobus_data.pop("ubicacion_actual_id")
        ubicacion_actual = Estacion.query.get_or_404(ubicacion_actual_id)

        autobus = Autobuses(ubicacion_actual=ubicacion_actual, **autobus_data)

        try:
            db.session.add(autobus)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return autobus
