import pytest

from app.models.models import Cliente, Modelo, Estado, Peticion
from app.services.add_car_from_request import AddCarRequest
from app.services.register_car import RegisterCar


class TestRequestPeticion:
    @pytest.fixture
    def service_register_car(self, repository):
        return RegisterCar(repository)

    @pytest.fixture
    def service_add_car_request(self, repository_peticion, repository, service_register_car):
        return AddCarRequest(repositorio_peticion=repository_peticion, repositorio_coche=repository, register_car=service_register_car)


    def test_request_peticion(self, service_register_car, repository_peticion, repository, service_add_car_request,
                              app):
        with app.app_context():
            modelo1 = Modelo(nombre='aaa', marca='bbb')
            cliente1 = Cliente(importe_disponible=100_000, nombre="Nilo")
            peticion1 = Peticion(cliente=cliente1, modelo=modelo1)
            repository_peticion.add(peticion1)

            service_add_car_request(peticion_id=peticion1.id)
            assert repository_peticion.get_by_id(id=peticion1.id) is None
            assert any([coche for coche in repository.get_all() if
                        coche.modelo.nombre == modelo1.nombre and coche.modelo.marca == modelo1.marca and coche.estado == Estado.DISPONIBLE])
