import inspect
import logging
from json import JSONDecodeError as JSONDecodeException
from typing import Callable

from aiohttp.web_request import Request

from .schema import SchemaModel  
from .exceptions import APIError, ClassBaseError 

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d')


class Route:
    
    def __init__(self, path: str, handler: Callable, method: str, name: str, **kwargs):
        self.path = path
        self.handler = handler
        self.method = method
        self.name = name
        self.kwargs = kwargs
        self.schema = None
        if self.kwargs.get('schema', None) is not None:
            if inspect.isclass(self.kwargs['schema']):
                if issubclass(self.kwargs['schema'], SchemaModel):
                    self.schema = self.kwargs['schema']
                else:
                    raise ClassBaseError
            else:
                raise ClassBaseError

    async def __call__(self, request: Request):
        if self.method == request.method:
            if self.schema is not None:
                try:
                    data = await request.json()
                except JSONDecodeException:
                    data = {}
                try:
                    self.schema(data)
                except APIError as e:
                    raise e
            match_info = request.match_info
            return await self.handler(request, **match_info)
        else:
            raise APIError('MethodNotAllowed', 405)
    
    def __repr__(self):
        return f'<Route {self.method} {self.path}>'
    
    def __str__(self):
        return self.__repr__()
