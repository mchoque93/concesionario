import pytest

from app.infrastructure.sqlalchemy_repository import SQLRepository
from app.models.models import Coche, Cliente, Transaccion, Peticion, Modelo


@pytest.fixture
def repository():
    return SQLRepository(Coche)


@pytest.fixture
def repository_cliente():
    return SQLRepository(Cliente)


@pytest.fixture
def repository_transaccion():
    return SQLRepository(Transaccion)


@pytest.fixture
def repository_peticion():
    return SQLRepository(Peticion)


@pytest.fixture
def repository_modelo():
    return SQLRepository(Modelo)
