from flask_marshmallow import Schema
from marshmallow import fields

class ClienteSchema(Schema):
    id = fields.Integer(dump_only=True)
    importe_disponible = fields.Integer(required=False)
    nombre = fields.String(required=False)
    transacciones = fields.String(required=False, many=True)
    peticiones = fields.String(required=False, many=True)

class InputClienteSchema(Schema):
    importe_disponible = fields.Integer(required=False)
    nombre = fields.String(required=False)

class ModeloSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=False)
    marca = fields.String(required=False)

modelo_schema=ModeloSchema()
class CocheSchema(Schema):
    id = fields.Integer(dump_only=True)
    estado = fields.Integer(required=False)
    matricula = fields.String(required=False)
    precio = fields.Integer(required=False)
    modelo = fields.Nested(ModeloSchema)

class BuyerSchema(Schema):
    coche_id = fields.Integer(required=False)
    cliente_id = fields.Integer(required=False)
    importe_abonado = fields.Integer(required=False)

class TransaccionSchema(Schema):
    id = fields.Integer(dump_only=True)
    coche = fields.Nested(CocheSchema)
    cliente = fields.Nested(ClienteSchema)
    importe_abonado = fields.Integer(required=False)

class PeticionSchema(Schema):
    cliente_id = fields.Integer(required=False)
    modelo_id = fields.Integer(required=False)

