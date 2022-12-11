import pytest

from app.infrastructure.sqlalchemy_repository import SQLRepository
from app.models.models import Coche, Estado, Modelo, Cliente, Transaccion, Peticion
from app.services.cliente_buy_car import BuyCar
from app.services.register_cliente import RegisterCliente
from app.services.request_peticiones import RequestPeticion


class TestSQLServices:

    @pytest.fixture
    def repository(self):
        return SQLRepository(Coche)

    @pytest.fixture
    def repository_cliente(self):
        return SQLRepository(Cliente)

    @pytest.fixture
    def repository_transaccion(self):
        return SQLRepository(Transaccion)

    @pytest.fixture
    def repository_peticion(self):
        return SQLRepository(Peticion)

    @pytest.fixture
    def repository_modelo(self):
        return SQLRepository(Modelo)

    @pytest.fixture
    def service(self, repository):
        return RegisterCliente(repository)

    @pytest.fixture
    def service_coche(self, repository, repository_cliente, repository_transaccion):
        return BuyCar(repositorio_coche=repository, repositorio_cliente=repository_cliente,
                      repositorio_transaccion=repository_transaccion)

    @pytest.fixture
    def service_add_requests(self, repository_peticion, repository, repository_modelo):
        return RequestPeticion(repositorio_peticion=repository_peticion, repositorio_cliente=repository, repositorio_modelo=repository_modelo)

    def test_register_cliente(self, repository_cliente, service, app):
        with app.app_context():
            cliente1 = Cliente(importe_disponible=100_000, nombre="Nilo")
            service.register_cliente(importe_disponible=100_000, nombre="Nilo")
            assert len([cliente for cliente in repository_cliente.get_all() if
                        (cliente.importe_disponible == cliente1.importe_disponible) and (
                                cliente.nombre == cliente1.nombre)]) != 0

    def test_register_transaccion(self, repository, repository_cliente, repository_transaccion, service_coche, app):
        with app.app_context():
            cliente1 = Cliente(importe_disponible=100_000, nombre="Nilo")
            modelo = Modelo(nombre='aaa', marca='bbb')
            coche1 = Coche(estado=Estado.DISPONIBLE, matricula="aaa", precio=100_000, modelo=modelo)

            repository.add(coche1)
            repository_cliente.add(cliente1)

            coche = repository.get_by_id(id=coche1.id)
            cliente = repository_cliente.get_by_id(id=cliente1.id)

            service_coche.buy_a_car(cliente_id=cliente1.id, coche_id=coche1.id, importe_abonado=100_000)

            assert len([transaccion for transaccion in repository_transaccion.get_all() if
                        (transaccion.importe_abonado == 100_000) and (cliente.id == cliente1.id) and (
                                coche.id == coche1.id)]) != 0
            assert repository.get_by_id(id=coche1.id).estado == Estado.VENDIDO


    def test_register_peticion(self, repository_cliente, repository_peticion, repository_modelo, service_add_requests, app):
        with app.app_context():
            cliente1 = Cliente(importe_disponible=100_000, nombre="Nilo")
            modelo1 = Modelo(nombre='aaa', marca='bbb')

            repository_modelo.add(modelo1)
            repository_cliente.add(cliente1)

            modelo = repository_modelo.get_by_id(id=modelo1.id)
            cliente = repository_cliente.get_by_id(id=cliente1.id)

            service_add_requests.add_peticion(modelo_id=modelo1.id, cliente_id=cliente1.id)
            assert len([peticion for peticion in repository_peticion.get_all() if
                        (modelo.id == modelo1.id) and (
                                cliente.id == cliente.id)]) != 0
