from apiflask import Schema
from apiflask.fields import String, Integer
from apiflask.validators import Length


class FootboolerInSchema(Schema):
    name = String(required=True, validate=Length(min=3, max=10))
    surname = String()


class FootboolerOutSchema(Schema):
    id_ = Integer()
    name = String()
    surname = String()
