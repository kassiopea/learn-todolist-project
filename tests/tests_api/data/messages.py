# class UserAuthMessages:
#     REVOKED_TOKEN = "Токен отозван"


class UserAuthErrors:
    FIELD_REQUIREMENT = "Поле обязательно для заполнения"
    ADMIN_NOT_REGISTRATION = "Пользователь с ролью админ не создан"
    # ERROR_REQUIRED_FIELD = 'Missing data for required field.'
    USERNAME_LENGTH = "Имя пользователя должно быть от 2 до 120 символов"
    PASSWORD_LENGTH = "Пароль должен быть от 6 до 20 символов"
    USERNAME_INVALID_SYMBOLS = "Имя пользователя должно содержать цифры, " \
                               "латинские буквы, символы:  '-_.'"
    EMAIL_INVALID = "Введен невалидный формат емейла"
    PASSWORD_INVALID = "Пароль должен содержать цифры, латинские буквы, символы: '-_:;!?()$#'"
    ADMIN_NOT_REGISTRATION = "Пользователь с ролью админ не создан"
    CREDENTIALS_REQUIREMENT = "Поля логин и пароль обязательны для заполнения"

    # ERROR_INVALID_USERNAME = 'Имя пользователя содержит недопустимые символы'
    # ERROR_INVALID_EMAIL = 'Not a valid email address.'
    # ERROR_INVALID_PASSWORD = 'Пароль содержит недопустимые символы'
    # ERROR_USER_ALREADY_EXIST = "Пользователь с таким имененм или " \
    #                            "почтой уже существует"
    # ERROR_REQUIRED_LOGIN_FIELDS = "Поля логин и пароль обязательны" \
    #                               " для заполнения"
    # ERROR_USER_NOT_FOUND = "Такого пользователя не существует"
    # ERROR_WITHOUT_AUTH_HEADER = "Missing Authorization Header"
    # ERROR_INVALID_TOKEN = "Signature verification failed"
    # ERROR_REVOKE_TOKEN = "Token has been revoked"
    # ERROR_REQUIRED_CHANGE_PWD = "Текущий пароль и новый пароль " \
    #                             "являются обязательными полями."
    # ERROR_INVALID_OLD_PWD = "Вы ввели неправильный пароль."
    # ERROR_OLD_PWD_EQUALS_NEW_PWD = "Пароль не был изменен. " \
    #                                "Новый пароль совпадает с текущим."


# class AuthErrors:
#     AUTH_NONE_TOKEN = "Missing Authorization Header"
#
#
# class TodoErrors:
#     ERROR_REQUIRED_PROJECT_NAME_FIELD = "Имя проекта обзяатльное поле."
#     ERROR_REQUIRED_FIELD = "Не заполнено обязательное поле."
