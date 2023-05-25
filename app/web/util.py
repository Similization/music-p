from typing import Any

from aiohttp.web_response import json_response as aiohttp_json_response


def json_response(data: Any = None, status: str = "ok"):
    if data is None:
        data = {}
    return aiohttp_json_response(
        data={
            "data": data,
            "status": status
        }
    )


def error_json_response(http_status: int, data: Any | None = None, status: str = "error",  message: str | None = None):
    if data is None:
        data = {}
    return aiohttp_json_response(
        status=http_status,
        data={
            "data": data,
            "status": status,
            "message": message
        }
    )
