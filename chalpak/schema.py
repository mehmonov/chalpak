from .exceptions import APIError
from .response import JSONResponse


class SchemaModel:

    def __init__(self, data: dict):
        self._parse_model(data)

    @property
    def __response__(self):
        result = self.__dict__
        return JSONResponse(result).__response__

    def _parse_model(self, data):
        for key, annotate in self.__annotations__.items():
            if key in data:
                item = data.get(key)
                if isinstance(item, annotate):
                    self.__setattr__(key, item)
                else:
                    raise APIError('FieldTypeError', 400,
                                   f'{self.__class__.__name__} {key} is must be a {annotate.__name__}')
            else:
                if not hasattr(self, key):
                    raise APIError('FieldTypeError', 400, f'{self.__class__.__name__} {key} must be provided')
        return self

    def __repr__(self):
        return str(self.__dict__)