from ..default_button import DefaultButton


class StatusButton(DefaultButton):
    _status: str
    _available_status: tuple = ('normal', 'fail', 'success')

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        if value not in self._available_status:
            raise ValueError(f'{self.__class__.__name__}: status {value} not valid, '
                             f'only {self._available_status} available')

        self._status = value
        self.background_normal = f'resources/{self._status}_status_button_normal.png'
        self.background_down = f'resources/{self._status}_status_button_down.png'

    @status.deleter
    def status(self):
        self.status = 'normal'
