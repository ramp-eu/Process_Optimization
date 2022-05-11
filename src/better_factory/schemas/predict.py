from marshmallow import Schema, fields


class PredictInputSchema(Schema):
    model = fields.Str(required=True)
    data = fields.List(fields.Dict())


class PredictResponseSchema(Schema):
    predictions = fields.List(fields.Float())


class OptimizeInputSchema(Schema):
    model = fields.Str(required=True)
    data = fields.List(fields.Dict())
    optim_limits = fields.Dict()
    setpoints = fields.Dict()


class OptimizeResponseSchema(Schema):
    optimizations = fields.Dict()