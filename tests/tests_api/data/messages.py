class UserAuthMessages:
    REVOKED_TOKEN = "access_token был отозван"


class UserAuthErrors:
    FIELD_REQUIREMENT = "Поле обязательно для заполнения"
    ADMIN_NOT_REGISTRATION = "Пользователь с ролью админ не создан"
    USERNAME_LENGTH = "Имя пользователя должно быть от 2 до 120 символов"
    PASSWORD_LENGTH = "Пароль должен быть от 6 до 20 символов"
    USERNAME_INVALID_SYMBOLS = "Имя пользователя должно содержать цифры, " \
                               "латинские буквы, символы:  '-_.'"
    EMAIL_INVALID = "Введен невалидный формат емейла"
    PASSWORD_INVALID = "Пароль должен содержать цифры, латинские буквы, символы: '-_:;!?()$#'&"
    CREDENTIALS_REQUIREMENT = "Поля логин и пароль обязательны для заполнения"
    LOGIN_DOES_NOT_EXIST = "Такого пользователя не существует"
    MISSING_COOKIE_ACCESS_TOKEN = 'Missing cookie "access_token"'
    MISSING_CSRF_TOKEN = "Missing CSRF token"
    INVALID_TOKEN_IN_COOKIE = "Invalid crypto padding"
    INVALID_CSRF_TOKEN = "CSRF double submit tokens do not match"
    REVOKED_TOKEN = "Token has been revoked"
    INCORRECT_PASSWORD = "Такого пароля не существует."
    PASSWORD_DID_NOT_CHANGE = "Пароль не был изменен"
