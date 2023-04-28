class _BaseConnector:
    _user: str
    _password: str
    _database: str
    _host: str

    def __init__(self, user: str, password: str, database: str, host: str):
        self._user = user
        self._password = password
        self._database = database
        self._host = host
