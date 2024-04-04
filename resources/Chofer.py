from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import Choferes
from schemas import ChoferSchema

blp = Blueprint("choferes", "choferes", description="Operaciones en choferes")


@blp.route("/chofer/<int:chofer_id>")
class Chofer(MethodView):
    @blp.response(200, ChoferSchema)
    def get(self, chofer_id):
        chofer = Choferes.query.get_or_404(chofer_id)
        return chofer

    def delete(self, chofer_id):
        chofer = Choferes.query.get_or_404(chofer_id)
        db.session.delete(chofer)
        db.session.commit()
        return {"mensaje": "Chofer eliminado"}


@blp.route("/chofer")
class ListaChoferes(MethodView):
    @blp.response(200, ChoferSchema(many=True))
    def get(self):
        choferes = Choferes.query.all()
        return choferes

    @blp.arguments(ChoferSchema)
    @blp.response(201, ChoferSchema)
    def post(self, chofer_data):
        chofer = Choferes(**chofer_data)

        try:
            db.session.add(chofer)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return chofer
