from abc import abstractmethod
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.models import models

class AbstractRepository:
    @abstractmethod
    def add(self, data):
        raise NotImplemented

    @abstractmethod
    def get_by_id(self, data, id: int):
        raise NotImplemented

    @abstractmethod
    def get_all(self, data):
        raise NotImplemented

    @abstractmethod
    def register_cliente(self, importe_disponible:float, nombre:str):
        raise NotImplemented

