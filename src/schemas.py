from marshmallow import Schema, ValidationError, fields

__all__ = ('ValidationError', 'ConvertRequestSchema',)


class ConvertRequestSchema(Schema):
    from_currency = fields.Str(data_key='from', required=True)
    to_currency = fields.Str(data_key='to', required=True)
    amount = fields.Decimal(required=True)
