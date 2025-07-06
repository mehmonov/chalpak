from .exceptions import APIError

class SchemaModel(dict):
    """
    A base model for data validation that inherits from dict.

    It uses Python's type hints to validate the incoming data.
    """
    def __init__(self, data: dict):
        super().__init__()
        self._parse_model(data)

    def _parse_model(self, data: dict):
        """
        Parses and validates the input data against the model's annotations.
        """
        for key, expected_type in self.__annotations__.items():
            if key not in data and not hasattr(self, key):
                raise APIError(
                    'ValidationError', 400,
                    f"'{key}' is a required field in {self.__class__.__name__}."
                )
            
            if key in data:
                value = data[key]
                if not isinstance(value, expected_type):
                    raise APIError(
                        'ValidationError', 400,
                        f"'{key}' in {self.__class__.__name__} must be of type {expected_type.__name__}, but got {type(value).__name__}."
                    )
                self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        self[key] = value
