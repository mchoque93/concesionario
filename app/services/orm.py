from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import mapper, relationship

from app.models.models import Coche, Transaccion, Cliente, Peticion, Modelo

db = SQLAlchemy()
metadata = db.metadata

coche = Table("coche",
              metadata,
              Column("id", Integer, primary_key=True, autoincrement=True),
              Column("matricula", String),
              Column("precio", Float),
              Column("estado", Integer),
              Column("modelo_id", Integer, ForeignKey("modelo.id")))

modelo = Table("modelo",
               metadata,
               Column("id", Integer, primary_key=True, autoincrement=True),
               Column("nombre", String),
               Column("marca", String))

transaccion = Table("transaccion",
                    metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("coche_id", String, ForeignKey("coche.id")),
                    Column("cliente", String, ForeignKey("cliente.id")),
                    Column("importe_abonado", Float),
                    )

cliente = Table("cliente",
                metadata,
                Column("id", Integer, primary_key=True, autoincrement=True),
                Column("importe_disponible", Integer),
                Column("nombre", String))

peticion = Table("peticion",
                 metadata,
                 Column("id", Integer, primary_key=True, autoincrement=True),
                 Column("cliente", String), ForeignKey("cliente.id"),
                 Column("modelo", String, ForeignKey("modelo.id"))
                 )

def start_mappers():
    #modelo
    modelo_mapper = mapper(Modelo, modelo)

    #coche
    coche_mapper = mapper(Coche, coche,
                                properties={'modelo': relationship(modelo_mapper, backref="coche")})

    #cliente
    cliente_mapper = mapper(Cliente, cliente)

    #transaccion
    transaccion_mapper = mapper(Transaccion, transaccion,
                                properties={'coche': relationship(coche_mapper, backref="transaccion"),
                                            'cliente': relationship(cliente_mapper, backref="transaccion")})

    #peticion
    peticion_mapper = mapper(Peticion, peticion,
                                properties={'modelo': relationship(modelo_mapper, backref="transaccion"),
                                            'cliente': relationship(cliente_mapper, backref="transaccion")})
