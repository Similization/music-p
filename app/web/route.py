from aiohttp.web import Application
from app.user.route import setup_routes as user_setup_routes


def setup_routes(app: Application):
    user_setup_routes(app=app)
