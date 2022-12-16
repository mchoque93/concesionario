import pytest

from app.models.models import Cliente
from app.services.register_cliente import RegisterCliente


class TestRegisterCliente:
    @pytest.fixture
    def service(self, repository_cliente):
        return RegisterCliente(repository_cliente)

    def test_register_cliente(self, repository_cliente, service, app):
        with app.app_context():
            cliente1 = Cliente(importe_disponible=100_000, nombre="Nilo")
            service(importe_disponible=100_000, nombre="Nilo")
            assert (
                len(
                    [
                        cliente
                        for cliente in repository_cliente.get_all()
                        if (cliente.importe_disponible == cliente1.importe_disponible)
                        and (cliente.nombre == cliente1.nombre)
                    ]
                )
                != 0
            )
