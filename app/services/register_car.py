from app.models.models import Coche, Modelo


class RegisterCar:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def register_car(self, estado: int, matricula: str, precio: int, nombre: str, marca: str):
        self.repositorio.add(Coche(estado=estado, matricula=matricula, precio=precio, modelo=Modelo(nombre=nombre, marca=marca)))