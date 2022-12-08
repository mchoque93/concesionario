from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper, relationship

from app.models.models import Coche, Transaccion, Cliente, Peticion

db = SQLAlchemy()
metadata = db.metadata

coche = Table("coche",
              metadata,
              Column("id", Integer, primary_key=True, autoincrement=True),
              Column("matricula", String),
              Column("estado", Integer))

transaccion = Table("transaccion",
                    metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("coche", String, ForeignKey("coche.id"))
                    )

cliente = Table("cliente",
                metadata,
                Column("id", Integer, primary_key=True, autoincrement=True),
                Column("importe_disponible",Integer),
                Column("transaccion", Integer, ForeignKey("transaccion.id")))

peticion = Table("peticion",
                  metadata,
                  Column("id", Integer, primary_key=True, autoincrement=True),
                  Column("cliente", String), ForeignKey("cliente.id"),
                  Column("coches", String, ForeignKey("coches.id"))
                  )

association_table = Table("association_table",
                          metadata,
                          Column("cliente_id", Integer, ForeignKey("transaccion.id"), primary_key=True))

association_table_peticion = Table("association_table_peticion",
                          metadata,
                          Column("peticion_id", Integer, ForeignKey("coche.id"), primary_key=True))


def start_mappers():
    coche_mapper = mapper(Coche, coche)

    transaccion_mapper = mapper(Transaccion, transaccion, properties={'coche': relationship(coche_mapper, backref="transaccion")})
    cliente_mapper = mapper(Cliente, cliente, properties={'transaccion': relationship(transaccion_mapper, secondary=association_table, backref="cliente")})
    peticion_mapper = mapper(Peticion, peticion, properties={'cliente': relationship(cliente_mapper, backref="peticion"),
                                                            'coche': relationship(coche_mapper, secondary=association_table_peticion, backref="peticion")})
