from app.models.models import Coche, Modelo, Estado, Transaccion


class BuyCar:
    def __init__(self, repositorio_coche, repositorio_cliente, repositorio_transaccion):
        self.repositorio_coche = repositorio_coche
        self.repositorio_cliente = repositorio_cliente
        self.repositorio_transaccion = repositorio_transaccion


    def buy_a_car(self, coche_id: int, cliente_id: int, importe_abonado: int):
        coche_vendido = self.repositorio_coche.get_by_id(id=coche_id)
        coche_vendido.estado = Estado.VENDIDO
        comprador = self.repositorio_cliente.get_by_id(id=cliente_id)
        self.repositorio_transaccion.add(Transaccion(coche=coche_vendido, cliente= comprador, importe_abonado= importe_abonado))
