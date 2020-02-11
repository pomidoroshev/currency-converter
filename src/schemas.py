from marshmallow import Schema, ValidationError, fields

__all__ = ('ValidationError', 'ConvertRequestSchema', 'RateSchema')


ConvertRequestSchema = Schema.from_dict({
    'from': fields.Str(data_key='from', required=True),
    'to': fields.Str(data_key='to', required=True),
    'amount': fields.Decimal(required=True),
})


class RateSchema(Schema):
    currency = fields.Str(required=True)
    rate = fields.Decimal(required=True)
