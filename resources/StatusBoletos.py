from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import StatusBoletos
from schemas import StatusBoletoSchema, StatusBoletoUpdateSchema

blp = Blueprint("StatusBoletos", __name__, description="Operaciones en estatus de boletos")


@blp.route("/status_boletos/<int:status_id>")
class StatusBoleto(MethodView):
    @jwt_required()
    @blp.response(200, StatusBoletoSchema)
    def get(self, status_id):
        status_boleto = StatusBoletos.query.get_or_404(status_id)
        return status_boleto

    @jwt_required()
    def delete(self, status_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Se requiere privilegio de administrador.")
            
        status_boleto = StatusBoletos.query.get_or_404(status_id)
        db.session.delete(status_boleto)
        db.session.commit()
        return {"mensaje": "Estatus de boleto eliminado."}

    @blp.arguments(StatusBoletoUpdateSchema)
    @blp.response(200, StatusBoletoSchema)
    def put(self, status_data, status_id):
        status_boleto = StatusBoletos.query.get(status_id)
        if status_boleto:
            status_boleto.nombre = status_data["nombre"]
        else:
            status_boleto = StatusBoletos(id=status_id, **status_data)
        
        db.session.add(status_boleto)
        db.session.commit()

        return status_boleto


@blp.route("/status_boletos")
class ListaDeStatusBoletos(MethodView):
    @jwt_required()
    @blp.response(200, StatusBoletoSchema(many=True))
    def get(self):
        return StatusBoletos.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(StatusBoletoSchema)
    @blp.response(201, StatusBoletoSchema)
    def post(self, status_data):
        status_boleto = StatusBoletos(**status_data)

        try:
            db.session.add(status_boleto)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Ocurrió un error al insertar el estatus de boleto.")

        return status_boleto
