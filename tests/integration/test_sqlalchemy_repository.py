import pytest

from app.infrastructure.sqlalchemy_repository import SQLRepository
from app.models.models import Coche, Estado, Modelo


class TestSQLRepository:
    @pytest.fixture
    def repository(self):
        return SQLRepository(Coche)

    def test_add(self, repository, app):
        with app.app_context():
            modelo1 = Modelo(nombre="Megane", marca="Renault")
            coche1 = Coche(
                estado=Estado.DISPONIBLE,
                matricula="51LKF",
                precio=20_000,
                modelo=modelo1,
            )
            repository.add(coche1)
            coches = repository.get_all()
            assert coches == [coche1]

    def test_get_all(self, repository, app):
        with app.app_context():
            modelo1 = Modelo(nombre="Megane", marca="Renault")
            coche1 = Coche(
                estado=Estado.DISPONIBLE,
                matricula="51LKF",
                precio=20_000,
                modelo=modelo1,
            )
            coche2 = Coche(
                estado=Estado.DISPONIBLE,
                matricula="50LKF",
                precio=20_000,
                modelo=modelo1,
            )
            coche3 = Coche(
                estado=Estado.DISPONIBLE,
                matricula="49LKF",
                precio=20_000,
                modelo=modelo1,
            )

            repository.add(coche1)
            repository.add(coche2)
            repository.add(coche3)

            assert len(repository.get_all()) == 3
            assert repository.get_all() == [coche1, coche2, coche3]

    def test_get_by_id(self, repository, app):
        with app.app_context():
            modelo1 = Modelo(nombre="Megane", marca="Renault")
            coche1 = Coche(
                estado=Estado.DISPONIBLE,
                matricula="51LKF",
                precio=20_000,
                modelo=modelo1,
            )
            repository.add(coche1)
            assert repository.get_by_id(id=1) == coche1
