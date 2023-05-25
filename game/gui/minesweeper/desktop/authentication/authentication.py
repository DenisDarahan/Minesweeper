from typing import Optional

from kivy.uix.checkbox import CheckBox
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest

from game.gui.api import server_api
from ...common import BasePopup
from .credentials_input import CredentialsInput


class Authentication(BasePopup):
    login_field: CredentialsInput = ObjectProperty()
    password_field: CredentialsInput = ObjectProperty()
    is_register: CheckBox = ObjectProperty()

    open_after_authentication: Optional[BasePopup.__class__]
    _login_dump: str

    def __init__(self, open_after_authentication: Optional[BasePopup.__class__] = None, **kwargs):
        super().__init__(**kwargs)

        self.open_after_authentication = open_after_authentication

    def on_pre_open(self):
        self.is_register.active = False

    def login(self):
        if not self.login_field.text:
            self.login_field.focus = True
            return
        if not self.password_field.text:
            self.password_field.focus = True
            return

        self._login_dump = self.login_field.text  # login can be edited

        if self.is_register.active:
            server_api.auth_sign_up(
                self._login_dump, self.password_field.text, self.auth_success, self.sign_up_failure, lambda *args: None)
        else:
            server_api.auth_sign_in(
                self._login_dump, self.password_field.text, self.auth_success, self.sign_in_failure, lambda *args: None)

    def auth_success(self, _req: UrlRequest, res: dict):
        server_api.access_token = res['access_token']

        del self._login_dump

        self.dismiss()
        if self.open_after_authentication:
            self.open_after_authentication().open()

    def sign_up_failure(self, req: UrlRequest, res: dict):
        if req.resp_status == 422:
            self.login_field.focus = True
            self.login_field.warning(res['detail'])

    def sign_in_failure(self, req: UrlRequest, res: dict):
        if req.resp_status == 401:
            if res['detail'] == 'Incorrect username':
                self.login_field.focus = True
                self.login_field.warning(res['detail'])
            elif res['detail'] == 'Incorrect password':
                self.password_field.focus = True
                self.password_field.warning(res['detail'])
