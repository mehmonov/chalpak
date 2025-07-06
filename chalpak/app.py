from aiohttp import web
from aiohttp.web import Request
from typing import Callable, List, Optional
import logging
import jinja2
import aiohttp_jinja2
from .routes import Route
from .response import HTMLResponse, Response, JSONResponse
from .exceptions import APIError

logging.basicConfig(level=logging.INFO)

class Chalpak:
    def __init__(self, host: str = "127.0.0.1", port: int = 6767, templates: Optional[str] = None, static_folder: Optional[str] = None) -> None:
        self.host = host
        self.port = port
        self.templates = templates
        self.static_folder = static_folder
        self.app = web.Application(middlewares=[self.error_middleware])
        self.routes: List[Route] = []

        if self.templates:
            aiohttp_jinja2.setup(self.app, loader=jinja2.FileSystemLoader(self.templates))

        if self.static_folder:
            self.app.router.add_static('/static/', path=self.static_folder, name='static')

    def _add_route(self, path: str, handler: Callable, method: str, name: str):
        route = Route(path, handler, method, name)
        self.routes.append(route)
        self.app.router.add_route(method, path, route)

    def get(self, path: str):
        def wrapper(func):
            async def decorated(request: Request, **kwargs):
                response = await func(request, **kwargs)
                return response.__response__ if isinstance(response, Response) else response

            self._add_route(path, decorated, 'GET', name=func.__name__)
            return decorated

        return wrapper

    def post(self, path: str):
        def wrapper(func):
            async def decorated(request: Request, **kwargs):
                response = await func(request, **kwargs)
                return response.__response__ if isinstance(response, Response) else response

            self._add_route(path, decorated, 'POST', name=func.__name__)
            return decorated

        return wrapper

    def put(self, path: str):
        def wrapper(func):
            async def decorated(request: Request, **kwargs):
                response = await func(request, **kwargs)
                return response.__response__ if isinstance(response, Response) else response

            self._add_route(path, decorated, 'PUT', name=func.__name__)
            return decorated

        return wrapper

    def delete(self, path: str):
        def wrapper(func):
            async def decorated(request: Request, **kwargs):
                response = await func(request, **kwargs)
                return response.__response__ if isinstance(response, Response) else response

            self._add_route(path, decorated, 'DELETE', name=func.__name__)
            return decorated

        return wrapper

    @web.middleware
    async def error_middleware(self, request: Request, handler: Callable):
        try:
            return await handler(request)
        except APIError as e:
            # Handle custom API errors
            return e.__response__
        except web.HTTPException as ex:
            # Handle aiohttp's built-in HTTP exceptions
            return JSONResponse(
                {"error": {"name": ex.reason, "message": ex.text}},
                status_code=ex.status,
            ).__response__
        except Exception as e:
            # Handle unexpected server errors
            logging.error(f"Unexpected error: {e}", exc_info=True)
            return JSONResponse(
                {"error": {"name": "InternalServerError", "message": "An unexpected error occurred."}},
                status_code=500,
            ).__response__

    def run(self):
        web.run_app(self.app, host=self.host, port=self.port)
