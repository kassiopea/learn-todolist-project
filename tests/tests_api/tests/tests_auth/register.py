import pytest
from pytest_schema import schema

from tests.tests_api.api_helpers.auth import ApiAuth
from tests.tests_api.constants import AuthUrls
from tests.tests_api.data.generate_auth_data import generate_data, generate_invalid_data
from tests.tests_api.data.messages import UserAuthErrors
from tests.tests_api.jsonSchema.auth import error_username, error_email, error_pwd
from tests.tests_api.models.user import User


class TestRegistrationWithoutRequiredFields:

    def test_check_response_without_username(
            self,
            get_base_header,
            get_user,
            base_url
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": get_user["email"],
            "password": get_user["password"]
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        content_type = response.headers["Content-Type"]
        assert content_type == "application/json"
        response_body = response.json()
        message = response_body["errors"][0]["username"]
        assert message == UserAuthErrors.FIELD_REQUIREMENT

    def test_check_json_schema_response_without_username(
            self,
            base_url,
            get_user,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": get_user["email"],
            "password": get_user["password"]
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        response_body = response.json()
        assert schema(error_username) == response_body

    def test_check_response_without_email(
            self,
            get_base_header,
            get_user,
            base_url
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_user["username"],
            "password": get_user["password"]
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        content_type = response.headers["Content-Type"]
        assert content_type == "application/json"
        response_body = response.json()
        message = response_body["errors"][0]["email"]
        assert message == UserAuthErrors.FIELD_REQUIREMENT

    def test_check_json_schema_response_without_email(
            self,
            base_url,
            get_user,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_user["username"],
            "password": get_user["password"]
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        response_body = response.json()
        assert schema(error_email) == response_body

    def test_check_response_without_password(
            self,
            get_base_header,
            get_user,
            base_url
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_user["username"],
            "email": get_user["email"]
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        content_type = response.headers["Content-Type"]
        assert content_type == "application/json"
        response_body = response.json()
        message = response_body["errors"][0]["password"]
        assert message == UserAuthErrors.FIELD_REQUIREMENT

    def test_check_json_schema_response_without_password(
            self,
            base_url,
            get_user,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_user["username"],
            "email": get_user["email"]
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        response_body = response.json()
        assert schema(error_pwd) == response_body


class TestRegistrationWithEmptyRequiredFields:

    @pytest.mark.parametrize("value", ["", " "])
    def test_check_response_with_empty_username(
            self,
            get_base_header,
            get_user,
            base_url,
            value
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": value,
            "email": get_user["email"],
            "password": get_user["password"]
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        content_type = response.headers["Content-Type"]
        assert content_type == "application/json"
        response_body = response.json()
        message = response_body["errors"][0]["username"]
        assert message == UserAuthErrors.FIELD_REQUIREMENT

    @pytest.mark.parametrize("value", ["", " "])
    def test_check_json_schema_response_wit_empty_username(
            self,
            base_url,
            get_user,
            get_base_header,
            value
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": value,
            "email": get_user["email"],
            "password": get_user["password"]
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        response_body = response.json()
        assert schema(error_username) == response_body

    @pytest.mark.parametrize("value", ["", " "])
    def test_check_response_with_empty_email(
            self,
            get_base_header,
            get_user,
            base_url,
            value
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_user["username"],
            "email": value,
            "password": get_user["password"]
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        content_type = response.headers["Content-Type"]
        assert content_type == "application/json"
        response_body = response.json()
        message = response_body["errors"][0]["email"]
        assert message == UserAuthErrors.FIELD_REQUIREMENT

    @pytest.mark.parametrize("value", ["", " "])
    def test_check_json_schema_response_with_empty_email(
            self,
            base_url,
            get_user,
            get_base_header,
            value
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_user["username"],
            "email": value,
            "password": get_user["password"]
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        response_body = response.json()
        assert schema(error_email) == response_body

    @pytest.mark.parametrize("value", ["", " "])
    def test_check_response_with_empty_password(
            self,
            get_base_header,
            get_user,
            base_url,
            value
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_user["username"],
            "email": get_user["email"],
            "password": value
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        content_type = response.headers["Content-Type"]
        assert content_type == "application/json"
        response_body = response.json()
        message = response_body["errors"][0]["password"]
        assert message == UserAuthErrors.FIELD_REQUIREMENT

    @pytest.mark.parametrize("value", ["", " "])
    def test_check_json_schema_response_with_empty_password(
            self,
            base_url,
            get_user,
            get_base_header,
            value
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_user["username"],
            "email": get_user["email"],
            "password": value
        }
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        response_body = response.json()
        assert schema(error_pwd) == response_body


class TestRegistrationInvalidWithBoundaryValues:
    def test_check_value_less_than_min_username(
            self,
            get_base_header,
            base_url,
            json_auth_invalid_boundary_name
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=json_auth_invalid_boundary_name["username"],
            email=generate_data("email", 8),
            password=generate_data("password", 7)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        message = response_body["errors"][0]["username"]
        assert message == UserAuthErrors.USERNAME_LENGTH

    def test_check_value_more_than_max_username(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data("username", 121),
            email=generate_data("email", 6),
            password=generate_data("password", 6)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        message = response_body["errors"][0]["username"]
        assert message == UserAuthErrors.USERNAME_LENGTH

    def test_check_value_less_than_min_password(
            self,
            get_base_header,
            base_url,
            json_auth_invalid_boundary_password
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data("username", 11),
            email=generate_data("email", 7),
            password=json_auth_invalid_boundary_password["password"]
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        message = response_body["errors"][0]["password"]
        assert message == UserAuthErrors.PASSWORD_LENGTH

    def test_check_value_more_than_max_password(
            self,
            get_base_header,
            base_url,
            json_auth_invalid_boundary_password
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data("username", 5),
            email=generate_data("email", 4),
            password=json_auth_invalid_boundary_password["password"]
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        message = response_body["errors"][0]["password"]
        assert message == UserAuthErrors.PASSWORD_LENGTH


class TestRegistrationInvalidValues:
    def test_check_invalid_username(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_invalid_data("username", 10),
            email=generate_data("email", 4),
            password=generate_data("password", 6)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        message = response_body["errors"][0]["username"]
        assert message == UserAuthErrors.USERNAME_INVALID_SYMBOLS

    def test_check_invalid_first_symbol_in_username(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_invalid_data("username_first_symbol", 8),
            email=generate_data("email", 4),
            password=generate_data("password", 12)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        message = response_body["errors"][0]["username"]
        assert message == UserAuthErrors.USERNAME_INVALID_SYMBOLS

    def test_check_invalid_email(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data("username", 4),
            email="test.test.ru",
            password=generate_data("password", 7)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        message = response_body["errors"][0]["email"]
        assert message == UserAuthErrors.EMAIL_INVALID

    def test_check_invalid_password(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data("username", 5),
            email=generate_data("email", 6),
            password=generate_invalid_data("password", 7)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        message = response_body["errors"][0]["password"]
        assert message == UserAuthErrors.PASSWORD_INVALID

    def test_check_invalid_admin_key(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data("username", 5),
            email=generate_data("email", 5),
            password=generate_data("password", 6),
            admin_key="test"
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        message = response_body["errors"][0]["admin_key"]
        assert message == UserAuthErrors.ADMIN_NOT_REGISTRATION

    def test_check_invalid_username_equal_deleted_user(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)

        response = auth.delete_user(
            path=AuthUrls.DELETE,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie

        )
        assert response.status_code == 200

        data = {
            "username": get_auth_user.username,
            "email": "testDelUsernameNew@teset.ru",
            "password": get_auth_user.password
        }

        response_for_register = auth.registration(
            path=AuthUrls.REGISTER,
            data=data
        )

        assert response_for_register.status_code == 400
        response_for_register_body = response_for_register.json()
        print(response_for_register_body)
        current_msg = response_for_register_body["errors"][0]["username"]
        assert current_msg == UserAuthErrors.USERNAME_ALREADY_EXISTS

    def test_check_invalid_email_equal_deleted_user(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)

        response = auth.delete_user(
            path=AuthUrls.DELETE,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie

        )
        assert response.status_code == 200

        data = {
            "username": "NewUserAsDeleted",
            "email": get_auth_user.email,
            "password": get_auth_user.password
        }

        response_for_register = auth.registration(
            path=AuthUrls.REGISTER,
            data=data
        )

        assert response_for_register.status_code == 400
        response_for_register_body = response_for_register.json()
        current_msg = response_for_register_body["errors"][0]["email"]
        assert current_msg == UserAuthErrors.USER_ALREADY_EXISTS


class TestRegistrationValidValue:
    def test_check_value_min_username(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data("username", 2),
            email=generate_data("email", 6),
            password=generate_data("password", 6)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 200
        assert "access_token" in response.cookies
        response_body = response.json()
        current_username = response_body["data"]["username"]
        assert current_username == get_user.username
        assert "access_token" in response.cookies

    def test_check_value_max_username(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data(field="username", length=120),
            email=generate_data("email", length=7),
            password=generate_data("password", 10)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 200
        response_body = response.json()
        current_username = response_body["data"]["username"]
        assert current_username == get_user.username
        assert "access_token" in response.cookies

    def test_check_min_value_password(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)

        get_user = User(
            username=generate_data("username", 12),
            email=generate_data("email", 4),
            password=generate_data("password", 6)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 200
        response_body = response.json()
        current_username = response_body["data"]["username"]
        assert current_username == get_user.username
        assert "access_token" in response.cookies

    def test_check_max_value_password(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data("username", 4),
            email=generate_data("email", 5),
            password=generate_data("password", 20)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 200
        response_body = response.json()
        current_username = response_body["data"]["username"]
        assert current_username == get_user.username
        assert "access_token" in response.cookies

    def test_check_average_length_value_username(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data("username", 8),
            email=generate_data("email", 6),
            password=generate_data("password", 6)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 200
        assert "access_token" in response.cookies
        response_body = response.json()
        current_username = response_body["data"]["username"]
        assert current_username == get_user.username
        assert "access_token" in response.cookies

    def test_check_average_length_value_password(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        get_user = User(
            username=generate_data("username", 6),
            email=generate_data("email", 6),
            password=generate_data("password", 8)
        )
        data = vars(get_user)
        response = auth.registration(
            path=AuthUrls.REGISTER,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 200
        assert "access_token" in response.cookies
        response_body = response.json()
        current_username = response_body["data"]["username"]
        assert current_username == get_user.username
        assert "access_token" in response.cookies
