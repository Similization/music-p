import typing

from app.store.user.accessor import UserAccessor

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_accessors(app: "Application"):
    app.user_accessor = UserAccessor()
    app.on_startup.append(app.user_accessor.connect)
    app.on_cleanup.append(app.user_accessor.disconnect)
