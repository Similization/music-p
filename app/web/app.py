from aiohttp.web import (
    Application as AiohttpApplication,
    View as AiohttpView,
    Request as AiohttpRequest,
    run_app as aiohttp_run_app,
)

from aiohttp_apispec import setup_aiohttp_apispec

from app.store import setup_accessors
from app.store.user.accessor import UserAccessor
from app.web.middleware import setup_middlewares
from app.web.route import setup_routes


class Application(AiohttpApplication):
    database: dict = {}
    user_accessor: UserAccessor | None = None


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app() -> Application:
    setup_routes(app=app)
    setup_aiohttp_apispec(app=app, url="docs/json", swagger_path="/docs")
    setup_accessors(app=app)
    setup_middlewares(app=app)
    aiohttp_run_app(app=app)
    return app
