from typing import Callable


class ErrorHandler:

    @classmethod
    def filter_list(cls, method: Callable) -> Callable:
        def decorator(self, *args, **kwargs) -> list:
            return [*filter(None, method(self, *args, **kwargs))]
        return decorator

    @classmethod
    def filter_dict(cls, method: Callable) -> Callable:
        def decorator(self, *args, **kwargs) -> dict:
            return method(self, *args, **kwargs) or {}
        return decorator
