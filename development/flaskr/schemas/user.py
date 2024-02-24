from marshmallow import fields
from marshmallow import Schema


class UserLoginRequest(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)


class AuthResponse(Schema):
    token = fields.String()
