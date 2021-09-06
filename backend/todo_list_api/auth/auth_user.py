from flask import request
from flask_jwt_extended import get_jwt

from todo_list_api.auth.helper import (
    authenticate,
    token_revoke,
    registration, remove_user, change_password
)
from todo_list_api.auth.messages import ErrorMessages
from todo_list_api.auth.validators import validate, RegisterUser, ChangePasswords
from todo_list_api.helpers.response import make_response
from todo_list_api.settings import ACCESS_EXPIRES


def register():
    username: str = request.form.get('username', None)
    email: str = request.form.get('email', None)
    password: str = request.form.get('password', None)
    admin_key: str = request.form.get('admin_key', None)

    current_user = RegisterUser(username, email, password, admin_key)
    errors = validate(current_user)

    if errors["errors"]:
        return make_response(data=None, error=errors["errors"], status_code=400)

    response = registration(
        current_user.admin_key,
        current_user.username,
        current_user.email,
        current_user.password
    )
    return response


def login():
    username: str = request.form.get('username', None)
    email: str = request.form.get('email', None)
    password: str = request.form.get('password', None)

    if password is not None:
        password = str(password.strip())
    if username is not None:
        username = str(username.strip())
    if email is not None:
        email = str(email.strip())

    if password is not None \
            and password != "" \
            and username is not None \
            and username != "":
        user = authenticate(login=username, password=password)
        return user
    elif password is not None \
            and password != "" \
            and email is not None \
            and email != "":
        user = authenticate(email, password)
        return user
    else:
        return make_response(error={"login": ErrorMessages.CREDENTIALS_REQUIREMENT}, status_code=400)


def logout():
    jti = get_jwt()["jti"]
    return token_revoke(jti, ACCESS_EXPIRES)


def change_pwd(user_id, data):
    old_password = data.get('old_password')
    new_password = data.get('new_password')

    passwords = ChangePasswords(old_password, new_password)
    errors = validate(passwords)
    if errors["errors"]:
        response = make_response(error=errors["errors"], status_code=400)
        return response

    response = change_password(user_id, passwords.old_password, passwords.new_password)
    return response


def delete_user_account(user_id):
    logout()
    response = remove_user(user_id)
    return response
