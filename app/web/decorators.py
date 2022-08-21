import functools
from aiohttp.web_exceptions import HTTPUnauthorized

from app.web.app import View


def auth_required():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(obj: View):
            if obj.request.admin is None:
                raise HTTPUnauthorized
            return await func(obj)
        return wrapped
    return wrapper
