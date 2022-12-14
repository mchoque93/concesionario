from unittest.mock import MagicMock

import pytest

from app.infrastructure.sqlalchemy_repository import SQLRepository
from app.models.models import Coche, Estado, Modelo, Cliente, Transaccion, Peticion
from app.services import add_car_from_request
from app.services.add_car_from_request import AddCarRequest
from app.services.cliente_buy_car import BuyCar
from app.services.register_car import RegisterCar
from app.services.register_cliente import RegisterCliente
from app.services.request_peticiones import RequestPeticion


class TestBuyACar:

    @pytest.fixture
    def repository_coche(self):
        return MagicMock()

    @pytest.fixture
    def repository_cliente(self):
        return MagicMock()

    @pytest.fixture
    def repository_transacciones(self):
        return MagicMock()

    @pytest.fixture
    def service_buy_a_car(self, repository_coche, repository_cliente, repository_transacciones):
        return BuyCar(repository_coche, repository_cliente, repository_transacciones)

    def test_fill_transacciones(self, service_buy_a_car, repository_coche, repository_cliente,
                                repository_transacciones):
        coche = Coche(estado=Estado.DISPONIBLE, matricula="aa", precio=1_000, modelo=Modelo(nombre="bb", marca="dd"))
        cliente = Cliente(importe_disponible=2_000, nombre="Nilo")
        transaccion = Transaccion(coche=coche, cliente=cliente, importe_abonado=1_000)

        repository_coche.get_by_id.return_value = coche
        repository_cliente.get_by_id.return_value = cliente

        service_buy_a_car(1, 2)

        repository_coche.get_by_id.assert_called_once_with(id=1)
        repository_cliente.get_by_id.assert_called_once_with(id=2)
        repository_transacciones.add.assert_called_once_with = transaccion

        assert coche.estado == Estado.VENDIDO
        assert cliente.importe_disponible == 1_000

    def test_buy_a_car_with_no_money(self, service_buy_a_car, repository_coche, repository_cliente):
        coche = Coche(estado=Estado.DISPONIBLE, matricula="aa", precio=1_000, modelo=Modelo(nombre="bb", marca="dd"))
        cliente = Cliente(importe_disponible=100, nombre="Nilo")

        repository_coche.get_by_id.return_value = coche
        repository_cliente.get_by_id.return_value = cliente

        with pytest.raises(Exception):
            service_buy_a_car(1, 2)

    def test_buy_a_car_already_saled(self, service_buy_a_car, repository_coche, repository_cliente,):
        coche = Coche(estado=Estado.VENDIDO, matricula="aa", precio=1_000, modelo=Modelo(nombre="bb", marca="dd"))
        cliente = Cliente(importe_disponible=100, nombre="Nilo")

        repository_coche.get_by_id.return_value = coche
        repository_cliente.get_by_id.return_value = cliente

        with pytest.raises(Exception):
            service_buy_a_car(1, 2)


