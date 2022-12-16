import pytest

from app.models.models import Cliente, Modelo, Coche, Estado
from app.services.cliente_buy_car import BuyCar
from app.services.request_peticiones import RequestPeticion


class TestRegisterPeticion:
    @pytest.fixture
    def service_add_requests(
        self, repository_peticion, repository_cliente, repository_modelo
    ):
        return RequestPeticion(
            repositorio_peticion=repository_peticion,
            repositorio_cliente=repository_cliente,
            repositorio_modelo=repository_modelo,
        )

    def test_register_peticion(
        self,
        repository_cliente,
        repository_peticion,
        repository_modelo,
        service_add_requests,
        app,
    ):
        with app.app_context():
            cliente1 = Cliente(importe_disponible=100_000, nombre="Nilo")
            modelo1 = Modelo(nombre="aaa", marca="bbb")

            repository_modelo.add(modelo1)
            repository_cliente.add(cliente1)

            modelo = repository_modelo.get_by_id(id=modelo1.id)
            cliente = repository_cliente.get_by_id(id=cliente1.id)

            service_add_requests(modelo_id=modelo1.id, cliente_id=cliente1.id)
            assert any(
                [
                    peticion
                    for peticion in repository_peticion.get_all()
                    if (modelo.id == modelo1.id) and (cliente.id == cliente.id)
                ]
            )
