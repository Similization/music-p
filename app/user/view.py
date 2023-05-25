import uuid
from typing import List

from aiohttp_apispec import docs, request_schema, response_schema, querystring_schema

from app.user.model import User
from app.user.shema import GetUserSchema, AddUserSchema, ResponseUserSchema, ResponseUserListSchema
from app.web.app import View
from app.web.util import json_response


class AddUserView(View):
    @docs(tags=['user'], summary='Create new user', description='Add new user to database')
    @request_schema(schema=AddUserSchema)
    @response_schema(schema=ResponseUserSchema, code=200)
    async def post(self):
        data = self.request["data"]
        user = User(
            id=uuid.uuid4(),
            nickname=data["nickname"],
            first_name=None,
            last_name=None,
            birth_date=None,
            phone=None,
            email=None,
            city=None,
        )
        await self.request.app.user_accessor.add_user(user=user)
        raw_user = {"id": str(user.id), "nickname": user.nickname}
        return json_response(data={"user": raw_user})


class GetUserView(View):
    @docs(tags=['user'], summary='Get user', description='Get user by id from database')
    @querystring_schema(schema=GetUserSchema)
    @response_schema(schema=ResponseUserSchema, code=200)
    async def get(self):
        user_id = uuid.UUID(self.request.query["id"])
        user: User | None = await self.request.app.user_accessor.get_user(
            user_id=user_id
        )
        raw_user = {"id": str(user.id), "nickname": user.nickname}
        return json_response(data={"user": raw_user})


class GetUserListView(View):
    @docs(tags=['user'], summary='Get user list', description='Get user list from database')
    @response_schema(schema=ResponseUserListSchema, code=200)
    async def get(self):
        user_list: List[User] | None = await self.request.app.user_accessor.get_user_list()
        raw_user = [
            {"id": str(user.id), "nickname": user.nickname} for user in user_list
        ]
        return json_response(data={"user_list": raw_user})
