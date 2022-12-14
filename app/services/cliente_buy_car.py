from app.models.models import Coche, Modelo, Estado, Transaccion


class BuyCar:
    def __init__(self, repositorio_coche, repositorio_cliente, repositorio_transaccion):
        self.repositorio_coche = repositorio_coche
        self.repositorio_cliente = repositorio_cliente
        self.repositorio_transaccion = repositorio_transaccion

    def __call__(self, coche_id: int, cliente_id: int):
        coche_vendido = self.repositorio_coche.get_by_id(id=coche_id)
        if coche_vendido.estado == Estado.VENDIDO:
            raise ValueError("El coche ya esta vendido")
        coche_vendido.estado = Estado.VENDIDO
        comprador = self.repositorio_cliente.get_by_id(id=cliente_id)
        comprador.importe_disponible -= coche_vendido.precio
        if comprador.importe_disponible <0:
            raise ValueError("El cliente no tiene dinero para comprar el coche")
        self.repositorio_transaccion.add(
            Transaccion(coche=coche_vendido, cliente=comprador, importe_abonado=coche_vendido.precio))
