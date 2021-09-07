import os
import json

import allure
import pytest
import requests

from tests.tests_api.api_helpers.auth import ApiAuth
from tests.tests_api.api_helpers.base import ApiBase
from tests.tests_api.constants import BaseUrls, AuthUrls, Headers
from tests.tests_api.data.generate_auth_data import generate_data
from tests.tests_api.models.user import User, RegisteredUser


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="http://localhost:5000", help="this is base url for api"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@allure.title('Передали базовый URL')
@pytest.fixture
def todo_list_with_base_url():
    base_url = BaseUrls.BASE_URL
    return ApiBase(base_url=base_url)


@pytest.fixture
def get_user():
    user = User(
        username=generate_data("username", 6),
        email=generate_data("email", 6),
        password=generate_data("password", 6)
    )
    return vars(user)


@pytest.fixture
def get_base_header():
    header = Headers.BASE_HEADERS
    return header


@pytest.fixture
def get_registered_user(base_url, get_base_header, get_user):
    auth = ApiAuth(base_url)
    data = get_user
    response = auth.registration(
        path=AuthUrls.REGISTER,
        data=data,
        headers=get_base_header
    )
    assert response.status_code == 200
    return get_user


@pytest.fixture
def get_auth_user(base_url, get_base_header, get_registered_user):
    get_user = RegisteredUser(
        username=get_registered_user["username"],
        email=get_registered_user["email"],
        password=get_registered_user["password"],
        headers=get_base_header
    )
    auth = ApiAuth(base_url)
    data = vars(get_user)

    response_auth = auth.login(
        path=AuthUrls.LOGIN,
        data=data,
        headers=get_base_header
    )
    cookies = response_auth.cookies
    get_user.cookie = cookies
    headers = Headers.AUTH_HEADERS
    xscrf_token = cookies["csrf_access_token"]
    headers['X-CSRF-TOKEN-ACCESS'] = xscrf_token
    get_user.headers = headers
    return get_user


@pytest.fixture
def get_auth_token(get_user, get_base_header, base_url):
    auth = ApiAuth(base_url)
    data = get_user
    response = auth.login(path="login", data=data, headers=get_base_header)
    cookies = response.cookies
    return cookies


@pytest.fixture
def get_xscrf_token(get_auth_token, get_base_header):
    xscrf_token = get_auth_token["csrf_access_token"]
    headers = get_base_header
    headers["X-CSRF-TOKEN-ACCESS"] = xscrf_token
    return headers


# @allure.title('Авторизация пользователя')
# @pytest.fixture
# def auth_token(todo_list_with_base_url, request):
#     auth = ApiAuth()
#     data_for_auth = User(username=generate_data("username", 8),
#                          email=generate_data("email", 10),
#                          password=generate_data("password", 6))
#     data = vars(data_for_auth)
#
#     # auth_url = f'{AuthUrls.AUTH}{AuthUrls.REGISTER}'
#     auth_url = "register"
#     headers = BaseHeaders.HEADERS
#     # response = todo_list_with_base_url.post(path=auth_url,
#     #                                    headers=headers,
#     #                                    data=data)
#     response = auth.registration(
#         path=auth_url,
#         headers=headers,
#         data=data
#     )
#
#     with allure.step(f'Создали нового пользователя с именем: '
#                      f'{data_for_auth.username}, '
#                      f'почтой: {data_for_auth.email},'
#                      f'паролем: {data_for_auth.password}'):
#         assert response.status_code == 200
#
#     login_url = "login"
#     data_for_login = {"username": data_for_auth.username, "password": data_for_auth.password}
#     # s.get('https://www.google.com')
#     response_login = auth.login(
#         path=login_url,
#         headers=headers,
#         data=data_for_login
#     )
#
#     assert response_login.status_code == 200
#     cookies = response_login.cookies
#     xcsrf = cookies['csrf_access_token']
#     header_token = {"X-CSRF-TOKEN-ACCESS": xcsrf}
#     # auth_token = 'Bearer ' + response_body['access_token']
#
#     # def delete_user():
#     #     url = f'{AuthUrls.AUTH}{AuthUrls.DELETE}'
#     #     headers_for_delete_user = {'Authorization': auth_token}
#     #     response_for_delete_user = todo_list_crud_api.delete(
#     #         path=url, headers=headers_for_delete_user)
#     #     with allure.step(f'Запрос отправлен. '
#     #                      f'Проверяем, что пользователь '
#     #                      f'{data_for_auth.username} удалён'):
#     #         assert response_for_delete_user.status_code == 200, \
#     #             f'Пользователь не был удалён. ' \
#     #             f'Status code is {response.status_code}'
#     #
#     # request.addfinalizer(delete_user)
#     return cookies, xcsrf
#
#

def load_from_json(file):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "data/{}.json".format(file))
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("json_"):
            module = load_from_json(fixture[5:])
            metafunc.parametrize(fixture,
                                 module,
                                 ids=[repr(id) for id in module])
