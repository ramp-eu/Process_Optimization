from marshmallow import Schema, fields


class TrainInputSchema(Schema):
    model = fields.Str(required=True)
    datasets = fields.List(
        fields.List(fields.Dict())
    )
    input_tags = fields.List(fields.Str())
    target_tag = fields.Str()


class TrainResponseSchema(Schema):
    model = fields.Str(required=True)
    status = fields.Str()