from marshmallow import Schema, fields


class AdminLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class AdminResponseSchema(Schema):
    id = fields.Integer(required=True)
    email = fields.Email(required=True)
