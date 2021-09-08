from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)

from todo_list_api.auth import auth_user
from todo_list_api.auth.auth_user import (
    logout,
    change_pwd,
    delete_user_account
)

auth = Blueprint('auth', __name__)


@auth.route('register', methods=['POST'])
def sing_up():
    return auth_user.register()


@auth.route('login', methods=['POST'])
def login():
    return auth_user.login()


@auth.route('logout', methods=['DELETE'])
@jwt_required()
def access_revoke():
    if request.method == 'DELETE':
        return logout()


@auth.route('delete', methods=['DELETE'])
@jwt_required()
def delete_account():
    if request.method == 'DELETE':
        current_id = get_jwt_identity()
        return delete_user_account(current_id)


@auth.route('change-password', methods=['PUT'])
@jwt_required()
def change_the_password():
    current_id = get_jwt_identity()
    data = request.form
    return change_pwd(current_id, data)


@auth.route("protected")
@jwt_required()
def protected():
    current_id = get_jwt_identity()
    return jsonify(foo=current_id)
