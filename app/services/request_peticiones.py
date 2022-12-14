from app.models.models import Coche, Modelo, Estado, Transaccion, Peticion


class RequestPeticion:
    def __init__(self, repositorio_peticion, repositorio_cliente, repositorio_modelo):
        self.repositorio_peticion = repositorio_peticion
        self.repositorio_cliente = repositorio_cliente
        self.repositorio_modelo = repositorio_modelo

    def add_peticion(self, cliente_id: int, modelo_id: int):
        cliente = self.repositorio_cliente.get_by_id(id=cliente_id)
        modelo = self.repositorio_modelo.get_by_id(id=modelo_id)
        self.repositorio_peticion.add(Peticion(cliente=cliente, modelo=modelo))
