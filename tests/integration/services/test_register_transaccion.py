import pytest

from app.models.models import Cliente, Modelo, Coche, Estado
from app.services.cliente_buy_car import BuyCar


class TestRegisterTransaccion:
    @pytest.fixture
    def service_coche(self, repository, repository_cliente, repository_transaccion):
        return BuyCar(
            repositorio_coche=repository,
            repositorio_cliente=repository_cliente,
            repositorio_transaccion=repository_transaccion,
        )

    def test_register_transaccion(
        self, repository, repository_cliente, repository_transaccion, service_coche, app
    ):
        with app.app_context():
            cliente1 = Cliente(importe_disponible=100_000, nombre="Nilo")
            modelo = Modelo(nombre="aaa", marca="bbb")
            coche1 = Coche(
                estado=Estado.DISPONIBLE, matricula="aaa", precio=100_000, modelo=modelo
            )

            repository.add(coche1)
            repository_cliente.add(cliente1)

            coche = repository.get_by_id(id=coche1.id)
            cliente = repository_cliente.get_by_id(id=cliente1.id)

            service_coche(cliente_id=cliente1.id, coche_id=coche1.id)

            assert any(
                [
                    transaccion
                    for transaccion in repository_transaccion.get_all()
                    if (transaccion.importe_abonado == 100_000)
                    and (cliente.id == cliente1.id)
                    and (coche.id == coche1.id)
                ]
            )
            assert repository.get_by_id(id=coche1.id).estado == Estado.VENDIDO
