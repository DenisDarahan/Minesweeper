import json
from typing import Callable
from urllib.parse import urlencode

from kivy.network.urlrequest import UrlRequest

from game.gui.settings import settings
from ._base_requests import _BaseRequests


class ServerAPI(_BaseRequests):

    _authorization_header: dict = {}

    @property
    def access_token(self) -> dict:
        return self._authorization_header

    @access_token.setter
    def access_token(self, value: str):
        self._authorization_header['Authorization'] = f'Bearer {value}'

    @access_token.deleter
    def access_token(self):
        self._authorization_header.pop('Authorization')

    def __init__(self):
        self.origin = settings.SERVER_API

    def create_rate(self, time: int, score: int, on_success: Callable = lambda *args: None,
                    on_failure: Callable = lambda *args: None, on_error: Callable = lambda *args: None) -> UrlRequest:
        endpoint = '/rate/create'
        data = json.dumps({
            'game_time': time,
            'game_score': score
        })
        headers = {
            **self.access_token,
            'Content-Type': 'application/json'
        }
        return self.post(endpoint, data, headers, on_success, on_failure, on_error)

    def rate_me(self, on_success: Callable, on_failure: Callable, on_error: Callable) -> UrlRequest:
        endpoint = '/rate/me'
        params = {}
        headers = {
            **self.access_token
        }
        return self.get(endpoint, params, headers, on_success, on_failure, on_error)

    def rate_top(self, *, limit: int = 10, offset: int = 0, on_success: Callable, on_failure: Callable,
                 on_error: Callable = lambda *args: None) -> UrlRequest:
        endpoint = '/rate/top'
        params = {
            'limit': limit,
            'offset': offset
        }
        headers = {
            **self.access_token
        }
        return self.get(endpoint, params, headers, on_success, on_failure, on_error)

    def user_login_exists(self, login: str, on_success: Callable, on_failure: Callable,
                          on_error: Callable) -> UrlRequest:
        endpoint = f'/user/login-exists/{login}'
        params = {}
        headers = {}
        return self.get(endpoint, params, headers, on_success, on_failure, on_error)

    def auth_sign_up(self, username: str, password: str, on_success: Callable, on_failure: Callable,
                     on_error: Callable) -> UrlRequest:
        endpoint = '/auth/sign-up'
        data = urlencode({
            'username': username,
            'password': password
        })
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        return self.post(endpoint, data, headers, on_success, on_failure, on_error)

    def auth_sign_in(self, username: str, password: str, on_success: Callable, on_failure: Callable,
                     on_error: Callable) -> UrlRequest:
        endpoint = '/auth/sign-in'
        data = urlencode({
            'username': username,
            'password': password
        })
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        return self.post(endpoint, data, headers, on_success, on_failure, on_error)
