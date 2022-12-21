from abc import abstractmethod


class AbstractRepository:
    @abstractmethod
    def add(self, object):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, data, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_all(self, data):
        raise NotImplementedError

    @abstractmethod
    def delete(self, object):
        raise NotImplementedError
