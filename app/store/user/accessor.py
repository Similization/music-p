import typing
import uuid

from app.user.model import User

if typing.TYPE_CHECKING:
    from app.web.app import Application


class UserAccessor:
    def __init__(self):
        self.app: Application | None = None

    async def connect(self, app: "Application"):
        self.app = app
        try:
            self.app.database["users"]
        except KeyError:
            self.app.database["users"] = []
        print("Connected to database")

    async def disconnect(self, app: "Application"):
        self.app = None
        print("Disconnected from database")

    async def add_user(self, user: User):
        self.app.database["users"].append(user)

    async def get_user(self, user_id: uuid.UUID) -> User | None:
        for user in self.app.database["users"]:
            if user.id == user_id:
                return user
        return None

    async def get_user_list(self) -> list[User]:
        return self.app.database["users"]

    async def update_user(self, user_id: uuid.UUID):
        pass

    async def delete_user(self, user_id: uuid.UUID) -> User | None:
        user: User | None = await self.get_user(user_id=user_id)
        if user:
            self.app.database["users"].remove(user)
        return user
