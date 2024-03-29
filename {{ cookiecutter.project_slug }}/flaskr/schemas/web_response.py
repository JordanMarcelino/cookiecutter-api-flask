from marshmallow import fields
from marshmallow import Schema


# Response information
class Status(Schema):
    code = fields.Integer(metadata={"description": "Error code"})
    message = fields.String(metadata={"description": "Error message"})


# Standard web response
class WebResponse(Schema):
    status = fields.Nested(Status)
    data = fields.Raw(allow_none=True)
