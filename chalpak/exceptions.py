from aiohttp.web_response import json_response


class APIError(Exception):
    status_code: int
    message: str = None
    headers: dict = None

    def __init__(self, name: str, status_code: int, message: dict = None, headers: dict = None):
        self.name = name
        self.status_code = status_code
        self.message = message
        self.headers = headers
        exception_data = {
            'error': {
                'name': name,
                'message': message
            },
            'data': {}
        }
        self.__response__ = json_response(exception_data, status=status_code, reason=message, headers=headers)


class ClassBaseError(Exception):
    status_code: int
    message: str = None
    headers: dict = None

    def __init_subclass__(cls, **kwargs):
        name = cls.__name__
        status_code = cls.__dict__.get('status_code', 400)
        message = cls.__dict__.get('message', None)
        headers = cls.__dict__.get('headers', {})
        cls.name = name
        cls.status_code = status_code
        cls.message = message
        cls.headers = headers
        exception_data = {
            'error': {
                'name': name,
                'message': message
            },
            'data': {}
        }
        cls.__response__ = json_response(exception_data, status=status_code, reason=message, headers=headers)