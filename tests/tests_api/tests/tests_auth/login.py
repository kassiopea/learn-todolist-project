from tests.tests_api.api_helpers.auth import ApiAuth
from tests.tests_api.constants import AuthUrls
from tests.tests_api.data.generate_auth_data import generate_data
from tests.tests_api.data.messages import UserAuthErrors
from tests.tests_api.models.user import User, RegisteredUser


class TestLoginWithoutRequiredFields:
    def test_check_login_without_login_with_pwd(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "password": get_registered_user["password"]
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_without_password_with_username(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_registered_user["username"]
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_without_password_with_email(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": get_registered_user["email"]
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_without_username_and_pwd(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": None,
            "password": None
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_without_email_and_pwd(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": None,
            "password": None
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT


class TestLoginWithEmptyRequiredFields:
    def test_check_login_with_empty_username(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": "",
            "password": get_registered_user["password"]
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_with_empty_email(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": "",
            "password": get_registered_user["password"]
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_with_empty_password_with_username(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_registered_user["username"],
            "password": ""
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_with_empty_password_with_email(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": get_registered_user["email"],
            "password": ""
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_with_empty_email_and_pwd(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": "",
            "password": ""
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_with_empty_username_and_pwd(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": "",
            "password": ""
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_with_only_spaces_username_and_pwd(
            self,
            base_url,
            get_base_header
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": "   ",
            "password": "     "
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT

    def test_check_login_with_only_spaces_email_and_pwd(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": "   ",
            "password": "     "
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.CREDENTIALS_REQUIREMENT


class TestLoginWithInvalidFields:
    def test_check_invalid_username(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_registered_user["username"] + "I",
            "password": get_registered_user["password"]
        }

        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )

        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.LOGIN_DOES_NOT_EXIST

    def test_check_invalid_email(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": "test" + get_registered_user["email"],
            "password": get_registered_user["password"]
        }

        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )

        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.LOGIN_DOES_NOT_EXIST

    def test_check_invalid_password_with_email(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": get_registered_user["email"],
            "password": "None" + get_registered_user["password"]
        }

        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )

        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.LOGIN_DOES_NOT_EXIST

    def test_check_invalid_password_with_username(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_registered_user["username"],
            "password": "None" + get_registered_user["password"]
        }

        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )

        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.LOGIN_DOES_NOT_EXIST

    def test_check_invalid_username_and_pwd(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_registered_user["username"] + "I",
            "password": get_registered_user["password"] + "TEST"
        }

        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )

        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.LOGIN_DOES_NOT_EXIST

    def test_check_invalid_email_and_pwd(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": "test" + get_registered_user["email"],
            "password": "test" + get_registered_user["password"]
        }

        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )

        assert response.status_code == 400
        response_body = response.json()
        assert response_body["data"] is None
        message = response_body["errors"]["login"]
        assert message == UserAuthErrors.LOGIN_DOES_NOT_EXIST


class TestInvalidLogin:
    def test_check_cannot_login_deleted_user(
            self,
            base_url,
            get_base_header,
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
            "password": get_auth_user.password
        }

        response_for_login = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )
        assert response_for_login.status_code == 400
        response_for_login_body = response_for_login.json()
        print(response_for_login_body)


class TestLoginWithValidFields:
    def test_check_login_with_valid_username_and_pwd(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_registered_user["username"],
            "password": get_registered_user["password"]
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )

        assert response.status_code == 200
        response_body = response.json()
        current_username = response_body["data"]["username"]
        current_status = response_body["data"]["status"]
        assert current_username == get_registered_user["username"]
        assert current_status == "LoggedIn"

    def test_check_login_with_valid_email_and_pwd(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": get_registered_user["email"],
            "password": get_registered_user["password"]
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )

        assert response.status_code == 200
        response_body = response.json()
        current_username = response_body["data"]["email"]
        current_status = response_body["data"]["status"]
        assert current_username == get_registered_user["email"]
        assert current_status == "LoggedIn"

    def test_check_tokens_after_login_with_valid_username_and_pwd(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "username": get_registered_user["username"],
            "password": get_registered_user["password"]
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )

        assert response.status_code == 200
        assert "Set-Cookie" in response.headers
        cookies = response.cookies
        assert "access_token", "csrf_access_token" in cookies

    def test_check_tokens_after_login_with_valid_email_and_pwd(
            self,
            base_url,
            get_base_header,
            get_registered_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "email": get_registered_user["email"],
            "password": get_registered_user["password"]
        }
        response = auth.login(
            path=AuthUrls.LOGIN,
            data=data,
            headers=get_base_header
        )

        assert response.status_code == 200
        assert "Set-Cookie" in response.headers
        cookies = response.cookies
        assert "access_token", "csrf_access_token" in cookies

