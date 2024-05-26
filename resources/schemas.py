from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    password = fields.Str(required=True, validate=validate.Length(min=6), load_only=True)  # Assuming minimum password length of 6 characters

