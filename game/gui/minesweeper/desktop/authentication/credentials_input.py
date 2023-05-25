from ...common import DefaultTextInput


class CredentialsInput(DefaultTextInput):

    def insert_text(self, substring: str, from_undo=False):
        if not (substring[-1].isalnum() or substring[-1] == '_'):
            substring = substring[:-1]
            self.warning('Symbol not allowed')
        return super().insert_text(substring, from_undo=from_undo)
