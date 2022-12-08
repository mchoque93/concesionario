from dataclasses import dataclass, field
from enum import IntEnum
from typing import List


class Estado(IntEnum):
    DISPONIBLE = 0
    VENDIDO = 1


@dataclass
class Coche:
    id: int = field(init=False)
    matricula: str
    modelo: str
    estado: int

@dataclass
class Transaccion:
    id: int = field(init=False)
    coche: str

@dataclass
class Cliente:
    id: int = field(init=False)
    importe_disponible: int
    transaccion: List["Transaccion"] = field(default_factory=list) #1 cliente puede tener varias transicciones

@dataclass
class Peticion:
    id: int = field(init=False)
    cliente: str #1 peticion es de 1 cliente
    coches: List["Coche"] = field(default_factory=list) #1 peticion puede ser de varios coches


