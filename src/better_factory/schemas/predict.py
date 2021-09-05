from marshmallow import Schema, fields


class PredictSchema(Schema):
    model = fields.Str(required=True)
    # inputs = fields.List()

