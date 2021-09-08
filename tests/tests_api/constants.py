class BaseUrls:
    BASE_URL = "http://localhost:5000"


class AuthUrls:
    AUTH = '/api/v1/auth/'
    LOGIN = 'login'
    LOGOUT = 'logout'
    REGISTER = 'register'
    DELETE = 'delete'
    CHANGE_PASSWORD = 'change-password'


class Headers:
    BASE_HEADERS = {
        'Content-Type': "application/x-www-form-urlencoded",
    }
    AUTH_HEADERS = {
        'Content-Type': "application/x-www-form-urlencoded",
        'X-CSRF-TOKEN-ACCESS': None
    }


class TodoUrls:
    TODO_API = '/api/v1/todo_list/'
    CREATE_PROJECT = 'projects'
    TODO = 'todo'


class UsersUrls:
    USERS_API = "/api/v1/users/"
    PROFILE = "profile"


class Colors:
    COLORS_API = ""
