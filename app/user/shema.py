from marshmallow import Schema, fields

from app.web.shema import OkResponseSchema


class GetUserSchema(Schema):
    id = fields.UUID(required=True)


class AddUserSchema(Schema):
    id = fields.UUID()
    nickname = fields.Str(required=True)


class UserSchema(Schema):
    user = fields.Nested(nested=AddUserSchema)


class ResponseUserSchema(OkResponseSchema):
    data = fields.Nested(nested=UserSchema)


class UserListSchema(Schema):
    user_list = fields.Nested(nested=UserSchema, many=True)


class ResponseUserListSchema(OkResponseSchema):
    data = fields.Nested(nested=UserListSchema)
