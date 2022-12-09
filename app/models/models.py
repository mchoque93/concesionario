from dataclasses import dataclass, field
from enum import IntEnum
from typing import List


class Estado(IntEnum):
    DISPONIBLE = 0
    VENDIDO = 1


@dataclass
class Coche:
    id: int = field(init=False)
    estado: int
    matricula: str
    precio: float
    modelo: "Modelo"

@dataclass
class Modelo:
    id: int = field(init=False)
    nombre: str
    marca: str

@dataclass
class Transaccion:
    id: int = field(init=False)
    coche: "Coche"
    cliente: "Cliente"
    importe_abonado: float

@dataclass
class Cliente:
    id: int = field(init=False)
    importe_disponible: int
    nombre: str
    transacciones: List["Transaccion"]
    peticiones: List["Peticion"]

@dataclass
class Peticion:
    id: int = field(init=False)
    cliente: "Cliente"
    modelo: "Modelo"


