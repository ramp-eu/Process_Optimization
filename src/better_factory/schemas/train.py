from marshmallow import Schema, fields


class TrainInputSchema(Schema):
    model = fields.Str(required=True)
    datasets = fields.List(
        fields.List(fields.Dict()),
        required=True
    )
    input_tags = fields.List(fields.Str(), required=True)
    target_tag = fields.Str(required=True)
    model_class = fields.Str()
    horizontal_past = fields.Int(required=True)
    horizontal_future = fields.Int(required=True)
    training = fields.Dict()


class TrainResponseSchema(Schema):
    model = fields.Str(required=True)
    status = fields.Str()