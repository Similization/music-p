import typing

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    from app.user.view import AddUserView
    from app.user.view import GetUserView
    from app.user.view import GetUserListView

    app.router.add_view("/add_user", AddUserView)
    app.router.add_view("/get_user", GetUserView)
    app.router.add_view("/get_user_list", GetUserListView)
