from marshmallow import Schema, fields


class PredictInputSchema(Schema):
    model = fields.Str(required=True)
    data = fields.List(fields.Dict())


class PredictResponseSchema(Schema):
    predictions = fields.List(fields.Float())