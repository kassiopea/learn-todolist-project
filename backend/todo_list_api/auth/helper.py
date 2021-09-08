from datetime import timezone, timedelta

from bson import ObjectId
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    set_access_cookies
)
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from todo_list_api.auth.messages import ErrorMessages
from todo_list_api.extentions import mongo, redis, jwt

from todo_list_api.helpers.notifications import Notifications
from todo_list_api.helpers.response import make_response


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token_in_redis = redis.get(jti)
    return token_in_redis is not None


def token_revoke(jti, type_token):
    redis.set(jti, "true", ex=type_token)
    data = 'access_token был отозван'
    response = make_response(data=data, status_code=200)
    return response


def get_refresh_token(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response


def get_token(user_id):
    access_token = create_access_token(identity=user_id)
    return access_token


def registration(admin_key, username, email, password):
    users_collection = mongo.db.users
    hashed_password = generate_password_hash(password)

    existing_username = users_collection.find_one({'username': username})
    existing_email = users_collection.find_one({'email': email})

    notification = Notifications("errors")

    if existing_username is not None:
        notification.add_notification(
            "username",
            ErrorMessages.USERNAME_ALREADY_EXISTS
        )

    if existing_email is not None:
        notification.add_notification(
            "email",
            ErrorMessages.USER_ALREADY_EXISTS
        )

    errors = notification.get_notifications()

    if not errors["errors"]:
        status = 'registered'

        if admin_key is None:
            is_admin = False
        else:
            is_admin = True

        date_creation = datetime.utcnow()
        last_login = False
        _id = users_collection.insert(
            {
                'username': username,
                'email': email,
                'password': hashed_password,
                'status': status,
                'is_admin': is_admin,
                'date_creation': date_creation,
                'last_login': last_login
            }
        )
        token = get_token(str(_id))
        data = {
            "username": username,
            "email": email,
            "status": status,
            "last_login": last_login
        }

        response = make_response(data=data, status_code=200)
        response.set_cookie('access_token', token)
        return response

    return make_response(error=errors, status_code=400)


def authenticate(login, password):
    users_collection = mongo.db.users
    user = users_collection.find_one(
        {"$or": [{"username": login},
                 {"email": login}]}
    )

    existing_username = users_collection.find_one({"username": login})
    existing_email = users_collection.find_one({"email": login})

    if existing_username and check_password_hash(user.get("password"), password):
        response = get_auth_without_deleted_users(
            login_key="username",
            login=login,
            existing_user=existing_username
        )
        return response

    elif existing_email and check_password_hash(user.get("password"), password):
        response = get_auth_without_deleted_users(
            login_key="email",
            login=login,
            existing_user=existing_email
        )
        return response
    else:
        return make_response(error={"login": ErrorMessages.LOGIN_DOES_NOT_EXIST}, status_code=400)


def change_password(user_id, old_password, new_password):
    users_collection = mongo.db.users
    hashed_password = generate_password_hash(new_password)

    user = users_collection.find_one(
        {'_id': ObjectId(user_id)}
    )

    if user and check_password_hash(user.get("password"), old_password):
        data = users_collection.update(
            {'_id': ObjectId(user_id)},
            {'$set': {
                "password": hashed_password
            }})
        status_code = 200
        response = make_response(data=data, status_code=status_code)
        return response
    else:
        error = {"password": ErrorMessages.INCORRECT_PASSWORD}
        status_code = 400
        response = make_response(error=error, status_code=status_code)
        return response


def remove_user(user_id):
    users_collection = mongo.db.users
    status = "deleted"
    users_collection.update(
        {'_id': ObjectId(user_id)},
        {'$set': {"status": status}}
    )
    data = {
        'user_id': str(user_id),
        'delete': 'ok'
    }
    return make_response(data=data, status_code=200)


def get_auth_without_deleted_users(login_key, login, existing_user):
    users_collection = mongo.db.users
    status = existing_user['status']
    if status == "deleted":
        notifications = Notifications("errors")
        error = notifications.add_notification(field=login_key, message=ErrorMessages.LOGIN_DOES_NOT_EXIST)
        status_code = 400
        response = make_response(error=error["errors"], status_code=status_code)
        return response
    else:
        _id = str(existing_user['_id'])
        status = "LoggedIn"
        last_login = datetime.utcnow()
        users_collection.update(
            {login_key: login},
            {
                '$set':
                    {
                        "last_login": last_login,
                        "status": status
                    }
            }
        )
        access_token = get_token(_id)
        data = {
            login_key: login,
            "status": status,
            "last_login": last_login
        }
        response = make_response(data=data, status_code=200)
        set_access_cookies(response, access_token)
        return response
