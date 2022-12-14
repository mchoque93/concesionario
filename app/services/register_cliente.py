from app.models.models import Cliente


class RegisterCliente:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def __call__(self, importe_disponible: int, nombre: str):
        self.repositorio.add(
            Cliente(importe_disponible=importe_disponible, nombre=nombre)
        )
