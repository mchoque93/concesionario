from app.api.resources import register_car
from app.models.models import Estado
from database import db


class AddCarRequest:
    def __init__(self, repositorio_peticion, repositorio_coche, register_car):
        self.repositorio_peticion = repositorio_peticion
        self.repositorio_coche = repositorio_coche
        self.register_car = register_car

    def __call__(self, peticion_id: int):
        peticion = self.repositorio_peticion.get_by_id(id=peticion_id)
        self.register_car(estado=Estado.DISPONIBLE, matricula="NA", precio=0,
                                       nombre=peticion.modelo.nombre, marca=peticion.modelo.marca)
        self.repositorio_peticion.delete(peticion)
