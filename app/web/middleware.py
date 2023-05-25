import json
import typing

from app.web.util import error_json_response

if typing.TYPE_CHECKING:
    from app.web.app import Application

from aiohttp_apispec.middlewares import validation_middleware
from aiohttp.web_middlewares import middleware

from aiohttp.web_exceptions import HTTPException, HTTPUnprocessableEntity


@middleware
async def error_handling_middleware(request, handler):
    try:
        response = await handler(request)
        return response
    except HTTPUnprocessableEntity as e:
        return error_json_response(http_status=400, message="Bad request", data=json.loads(e.text))
    except HTTPException as e:
        return error_json_response(http_status=e.status, message=str(e))
    except Exception as e:
        return error_json_response(http_status=500, message="Internal server error", data=str(e))


def setup_middlewares(app: "Application"):
    app.middlewares.append(error_handling_middleware)
    app.middlewares.append(validation_middleware)
