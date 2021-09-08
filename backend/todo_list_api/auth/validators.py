import re
from os import environ

from todo_list_api.auth.messages import ErrorMessages
from todo_list_api.helpers.notifications import Notifications


class User:
    def __init__(self):
        self.pattern_username = r'^[0-9a-zA-Z]+[0-9a-zA-Z-_.]+$'
        self.pattern_email = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
        self.pattern_password = r'[0-9a-zA-Z-_:;!?()$&#]+$'
        self.notification = Notifications("errors")

    def _valid_password(self, raw_password, field_name, notification):
        password = raw_password if raw_password is None else raw_password.strip()
        if password is None or password == "":
            notification.add_notification(field_name, ErrorMessages.FIELD_REQUIREMENT)
        elif type(password) != str:
            notification.add_notification(field_name, ErrorMessages.STRING_FIELD)
        elif len(password) < 6 or len(password) > 20:
            notification.add_notification(field_name, ErrorMessages.PASSWORD_LENGTH)
        elif not re.match(self.pattern_password, password):
            notification.add_notification(field_name, ErrorMessages.PASSWORD_INVALID)
        return password

    def get_notifications(self):
        return self.notification.get_notifications()


class RegisterUser(User):
    def __init__(self, raw_username, raw_email, raw_password, admin_key):
        super().__init__()
        self.notification = Notifications("errors")
        self.username = self._valid_username(raw_username)
        self.email = self._valid_email(raw_email)
        self.password = self._valid_password(raw_password, "password", self.notification)
        self.current_admin_key = environ.get('SECRET_KEY_FOR_ADMIN')
        self.admin_key = self._valid_admin_key(admin_key)

    def _valid_username(self, raw_username):
        field_name = "username"
        username = raw_username if raw_username is None else raw_username.strip()
        if username is None or username == "":
            self.notification.add_notification(field_name, ErrorMessages.FIELD_REQUIREMENT)
        elif type(username) != str:
            self.notification.add_notification(field_name, ErrorMessages.STRING_FIELD)
        elif len(username) < 2 or len(username) > 120:
            self.notification.add_notification(field_name, ErrorMessages.USERNAME_LENGTH)
        elif not re.match(self.pattern_username, username):
            self.notification.add_notification(field_name, ErrorMessages.USERNAME_INVALID_SYMBOLS)
        return username

    def _valid_email(self, raw_email):
        field_name = "email"
        email = raw_email if raw_email is None else raw_email.strip()
        if email is None or email == "":
            self.notification.add_notification(field_name, ErrorMessages.FIELD_REQUIREMENT)
        else:
            email = raw_email.strip()

        if type(email) != str:
            self.notification.add_notification(field_name, ErrorMessages.STRING_FIELD)
        elif not re.match(self.pattern_email, email):
            self.notification.add_notification(field_name, ErrorMessages.EMAIL_INVALID)
        return email

    def _valid_admin_key(self, admin_key):
        field_name = "admin_key"
        if admin_key != self.current_admin_key and admin_key is not None:
            self.notification.add_notification(field_name, ErrorMessages.ADMIN_NOT_REGISTRATION)
        return admin_key


class ChangePasswords(User):
    def __init__(self, raw_old_pwd, raw_new_password):
        super().__init__()
        self.notification = Notifications("errors")
        self.old_password = self._valid_password(raw_old_pwd, "old_password", self.notification)
        self.new_password = self._equals_passwords(raw_new_password)

    def _equals_passwords(self, raw_new_password):
        self.new_password = self._valid_password(raw_new_password, "new_password", self.notification)
        old_password = self.old_password if self.old_password is None else self.old_password.strip()
        new_password = self.new_password if self.new_password is None else self.new_password.strip()

        if (old_password and new_password) is not None \
                and (old_password and new_password) != "" \
                and old_password == new_password:
            self.notification.add_notification("password", ErrorMessages.PASSWORD_DID_NOT_CHANGE)
        return new_password


def validate(user):
    return user.get_notifications()
