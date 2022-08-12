from marshmallow import Schema, fields


class TrainInputSchema(Schema):
    model = fields.Str(required=True)
    datasets = fields.List(
        fields.List(fields.Dict()),
        required=True
    )
    input_tags = fields.List(fields.Str(), required=True)
    target_tags = fields.List(fields.Str(), required=True)
    model_class = fields.Str()
    horizon_past = fields.Int(required=True)
    horizon_future = fields.Int(required=True)
    training = fields.Dict()
    time_discretization = fields.Str()


class TrainResponseSchema(Schema):
    model = fields.Str(required=True)
    status = fields.Str()