import os

from apiflask import APIBlueprint
from flask import request, Blueprint
from flask_restful import Api, Resource

from app.api.scheme import ClienteSchema, InputClienteSchema
from app.infrastructure.sqlalchemy_repository import SQLRepository
from app.models.models import Cliente
from app.services.register_cliente import RegisterCliente

concesionario_v1_0_bp = APIBlueprint('concesionario_v1_0_bp', __name__, url_prefix='/concesionario')


cliente_schema = ClienteSchema()
repository = SQLRepository(Cliente)
register_cliente = RegisterCliente(repository)

@concesionario_v1_0_bp.post("/")
@concesionario_v1_0_bp.input(schema=InputClienteSchema(many=True))
@concesionario_v1_0_bp.output(schema=ClienteSchema(many=True))
def register_client(data):
    """
    Registrar cliente
    :return:
    """
    register_cliente.register_cliente(importe_disponible= data[0]['importe_disponible'], nombre= data[0]['nombre'])

@concesionario_v1_0_bp.get("/")
@concesionario_v1_0_bp.output(schema=ClienteSchema(many=True))
def get_all():
    """
    Observaciones de todos los clientes
    :return:
    """
    clientes = repository.get_all()
    result = cliente_schema.dump(clientes, many=True)
    return result

