class User:

    def __init__(self,
                 username: str = None,
                 email: str = None,
                 password: str = None,
                 admin_key: str = None
                 ) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.admin_key = admin_key

    def __repr__(self):
        return repr((
            self.username,
            self.email,
            self.password,
            self.admin_key
        ))

    def __eq__(self, other):
        return self.username == other.username \
               and self.email == other.email \
               and self.password == other.password


class RegisteredUser(User):
    def __init__(
            self,
            username: str = None,
            email: str = None,
            password: str = None,
            admin_key: str = None,
            cookie: str = None,
            headers: str = None
    ) -> None:
        super().__init__(
            username,
            email,
            password,
            admin_key
        )
        self.cookie = cookie
        self.headers = headers

    def __repr__(self):
        return repr((
            self.username,
            self.email,
            self.password,
            self.admin_key,
            self.cookie,
            self.headers
        ))

    def __eq__(self, other):
        return self.username == other.username \
               and self.email == other.email \
               and self.password == other.password \
               and self.cookie == other.cookie \
               and self.headers == other.headers
