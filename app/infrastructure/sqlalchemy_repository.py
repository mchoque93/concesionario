from app.infrastructure.abstract_repository import AbstractRepository
from app.models.models import Cliente
from app.infrastructure.orm import db


class SQLRepository(AbstractRepository):

    def __init__(self, clase):
        self.clase = clase

    def get_all(self):
        return db.session.query(self.clase).all()

    def get_by_id(self, id: int):
        return db.session.query(self.clase).filter_by(id=id).first()

    def add(self, object):
        db.session.add(object)
        db.session.commit()
