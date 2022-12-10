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