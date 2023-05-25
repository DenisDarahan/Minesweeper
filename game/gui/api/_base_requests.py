from typing import Callable, Any
from urllib.parse import urlencode

from kivy.logger import Logger
from kivy.network.urlrequest import UrlRequest


class _BaseRequests:
    origin: str

    def request_info(self, req: UrlRequest) -> tuple[str, str]:
        return req.url.replace(self.origin, ''), req._method.upper()  # noqa

    def log_success(self, callback: Callable) -> Callable:
        def decorator(req: UrlRequest, result: Any) -> Any:
            endpoint, method = self.request_info(req)
            Logger.info(f'{callback.__qualname__}: {method} {endpoint} {str(result)[:50]}')
            return callback(req, result)
        return decorator

    def log_failure(self, callback: Callable) -> Callable:
        def decorator(req: UrlRequest, result: Any) -> Any:
            endpoint, method = self.request_info(req)
            Logger.error(f'{callback.__qualname__}: {method} {endpoint} {str(result)[:50]}')
            return callback(req, result)
        return decorator

    def log_error(self, callback: Callable) -> Callable:
        def decorator(req: UrlRequest, error: Exception) -> Any:
            endpoint, method = self.request_info(req)
            Logger.critical(f'{callback.__qualname__}: {method} {endpoint} '
                            f'{error.__class__.__name__} ({", ".join(map(str, error.args))})')
            return callback(req, error)
        return decorator

    def get(self, endpoint: str, params: dict, headers: dict, on_success: Callable, on_failure: Callable,
            on_error: Callable) -> UrlRequest:
        if not isinstance(params, dict):
            Logger.error(f'{self.get.__qualname__}: Not available params format! dict expected, '
                         f'{params.__class__.__name__} got')
            raise ValueError(f'params cannot be {params.__class__.__name__}')

        Logger.info(f'{self.get.__name__.upper()}: {endpoint} => {params}')

        return UrlRequest(
            url=self.origin + endpoint + (f'?{urlencode(params)}' if params else ''),
            req_headers=headers,
            on_success=self.log_success(on_success),
            on_failure=self.log_failure(on_failure),
            on_error=self.log_error(on_error),
            method='GET',
            timeout=30,
            verify=False
        )

    def post(self, endpoint: str, data: str, headers: dict, on_success: Callable, on_failure: Callable,
             on_error: Callable) -> UrlRequest:
        Logger.info(f'{self.post.__name__.upper()}: {endpoint} => {data}')

        return UrlRequest(
            url=self.origin + endpoint,
            req_headers=headers,
            req_body=data,
            on_success=self.log_success(on_success),
            on_failure=self.log_failure(on_failure),
            on_error=self.log_error(on_error),
            method='POST',
            timeout=40,
            verify=False
        )
