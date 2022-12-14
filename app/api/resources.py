import os

from apiflask import APIBlueprint
from flask import request, Blueprint, Response
from flask_restful import Api, Resource

from app.api.scheme import ClienteSchema, InputClienteSchema, CocheSchema, BuyerSchema, TransaccionSchema, \
    PeticionSchema
from app.infrastructure.sqlalchemy_repository import SQLRepository
from app.models.models import Cliente, Modelo, Coche, Transaccion, Peticion
from app.services.cliente_buy_car import BuyCar
from app.services.register_car import RegisterCar
from app.services.register_cliente import RegisterCliente
from app.services.request_peticiones import RequestPeticion

concesionario_v1_0_bp = APIBlueprint('concesionario_v1_0_bp', __name__, url_prefix='/concesionario')

coche_schema = CocheSchema()
cliente_schema = ClienteSchema()
buyer_schema = BuyerSchema()

repository = SQLRepository(Cliente)
repository_coche = SQLRepository(Coche)
repository_transaccion = SQLRepository(Transaccion)
repository_modelo = SQLRepository(Modelo)
repository_peticion = SQLRepository(Peticion)

register_cliente = RegisterCliente(repository)
register_coche = RegisterCar(repository_coche)
buy_car_service = BuyCar(repository_coche, repository, repository_transaccion)
requests = RequestPeticion(repository_peticion, repository, repository_modelo)

@concesionario_v1_0_bp.post("/customers")
@concesionario_v1_0_bp.input(schema=InputClienteSchema)
def register_client(data):
    """
    Registrar cliente
    :return:
    """
    register_cliente.register_cliente(importe_disponible=data['importe_disponible'], nombre=data['nombre'])
    return Response(None, status=201, mimetype='application/json')


@concesionario_v1_0_bp.get("/customers")
@concesionario_v1_0_bp.output(schema=ClienteSchema(many=True))
def get_all():
    """
    Observaciones de todos los clientes
    :return:
    """
    clientes = repository.get_all()
    result = cliente_schema.dump(clientes, many=True)
    return result


@concesionario_v1_0_bp.post("/cars")
@concesionario_v1_0_bp.input(schema=CocheSchema)
def register_car(data):
    """
    Registrar coches
    :return:
    """
    register_coche.register_car(estado=data['estado'], matricula=data['matricula'], precio=data['precio'],
                                nombre=data['modelo']['nombre'], marca=data['modelo']['marca'])
    return Response(None, status=201, mimetype='application/json')


@concesionario_v1_0_bp.get("/cars")
@concesionario_v1_0_bp.output(schema=CocheSchema(many=True))
def get_all_coches():
    """
    Listado de coches
    :return:
    """
    coches = repository_coche.get_all()
    result = CocheSchema().dump(coches, many=True)
    return result


@concesionario_v1_0_bp.post("/cars/<int:car_id>/buy")
@concesionario_v1_0_bp.input(schema=BuyerSchema)
def buy_car(data, car_id):
    """
    Comprar un coche por un cliente
    :return:
    """
    buy_car_service.buy_a_car(cliente_id=data['cliente_id'], coche_id=car_id,
                             importe_abonado=data['importe_abonado'])

    return Response(None, status=201, mimetype='application/json')

@concesionario_v1_0_bp.post("/requests")
@concesionario_v1_0_bp.input(schema=PeticionSchema)
def peticion_cliente(data):
    """
    Registrar peticion de un cliente
    :return:
    """
    requests.add_peticion(data['cliente_id'], data['modelo_id'])
    return Response(None, status=201, mimetype='application/json')

@concesionario_v1_0_bp.get("/requets")
@concesionario_v1_0_bp.output(schema=PeticionSchema(many=True))
def get_all_peticiones():
    """
    Listado de peticiones
    :return:
    """
    peticiones = repository_peticion.get_all()
    result = PeticionSchema().dump(peticiones, many=True)
    return result

@concesionario_v1_0_bp.get("/transacciones")
@concesionario_v1_0_bp.output(schema=TransaccionSchema(many=True))
def get_all_transacciones():
    """
    Listado de transacciones
    :return:
    """
    transacciones = repository_transaccion.get_all()
    result = TransaccionSchema().dump(transacciones, many=True)
    return result

