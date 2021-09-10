from tests.tests_api.api_helpers.auth import ApiAuth
from tests.tests_api.constants import AuthUrls
from tests.tests_api.data.messages import UserAuthErrors
from tests.tests_api.helpers import get_list_keys_from_response


class TestUnsuccessfulPasswordChange:
    def test_check_change_pwd_without_fields(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)

        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )
        assert response.status_code == 400
        response_body = response.json()
        current_keys = get_list_keys_from_response(response_body["errors"])
        expected_keys = ["old_password", "new_password"]
        assert current_keys == expected_keys

        for error in response_body["errors"]:
            for key in error.keys():
                assert error[key] == UserAuthErrors.FIELD_REQUIREMENT

    def test_check_change_pwd_without_and_empty_fields(
            self,
            base_url,
            get_auth_user,
            json_auth_empty_change_pwd
    ):
        auth = ApiAuth(base_url=base_url)
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=json_auth_empty_change_pwd,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )
        assert response.status_code == 400
        response_body = response.json()
        current_keys = get_list_keys_from_response(response_body["errors"])
        expected_keys = ["old_password", "new_password"]
        assert current_keys == expected_keys

        for error in response_body["errors"]:
            for key in error.keys():
                assert error[key] == UserAuthErrors.FIELD_REQUIREMENT

    def test_check_change_pwd_without_old_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "new_password": f'{get_auth_user.password}1'
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 400
        response_body = response.json()
        current_msg = response_body["errors"][0]["old_password"]
        assert current_msg == UserAuthErrors.FIELD_REQUIREMENT

    def test_check_change_pwd_without_new_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 400
        response_body = response.json()
        current_msg = response_body["errors"][0]["new_password"]
        assert current_msg == UserAuthErrors.FIELD_REQUIREMENT

    def test_check_change_pwd_with_empty_old_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": "",
            "new_password": f"{get_auth_user.password}1"
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 400
        response_body = response.json()
        current_msg = response_body["errors"][0]["old_password"]
        assert current_msg == UserAuthErrors.FIELD_REQUIREMENT

    def test_check_change_pwd_with_empty_new_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": ""
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 400
        response_body = response.json()
        current_msg = response_body["errors"][0]["new_password"]
        assert current_msg == UserAuthErrors.FIELD_REQUIREMENT

    def test_check_change_pwd_with_invalid_old_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": f"{get_auth_user.password}1111",
            "new_password": f"{get_auth_user.password}New"
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 400
        response_body = response.json()
        current_msg = response_body["errors"]["old_password"]
        assert current_msg == UserAuthErrors.INCORRECT_PASSWORD

    def test_check_change_pwd_with_invalid_new_pwd(
            self,
            base_url,
            get_auth_user,
            json_auth_invalid_new_pwd
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": json_auth_invalid_new_pwd["new_password"]
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 400
        response_body = response.json()
        current_message = response_body["errors"][0]["new_password"]
        assert current_message == UserAuthErrors.PASSWORD_INVALID

    def test_check_change_pwd_with_less_than_min_length_new_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": "12345"
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 400
        response_body = response.json()
        current_message = response_body["errors"][0]["new_password"]
        assert current_message == UserAuthErrors.PASSWORD_LENGTH

    def test_check_change_pwd_with_more_than_max_length_new_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": "123456789ABCDSLDsldjd"
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 400
        response_body = response.json()
        current_message = response_body["errors"][0]["new_password"]
        assert current_message == UserAuthErrors.PASSWORD_LENGTH

    def test_check_change_pwd_with_equal_new_and_old_pws(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": get_auth_user.password
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 400
        response_body = response.json()
        current_msg = response_body["errors"][0]["password"]
        assert current_msg == UserAuthErrors.PASSWORD_DID_NOT_CHANGE

    def test_check_change_pwd_without_cookie(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": f"{get_auth_user.password}TEST"
        }

        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers
        )

        assert response.status_code == 401

    def test_check_change_pwd_without_xcsrf_token_in_headers(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": f"{get_auth_user.password}TEST"
        }

        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 401


class TestSuccessfulPasswordChange:
    def test_check_change_pwd_with_min_length_new_pwd(
            self,
            base_url,
            get_auth_user,
            json_auth_valid_min_length_pwd
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": json_auth_valid_min_length_pwd["new_password"]
        }

        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 200
        response_body = response.json()
        assert response_body["data"]["nModified"] == 1
        assert response_body["data"]["updatedExisting"] is True

    def test_check_change_pwd_with_max_length_new_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": "123-_:;!?()$#'&TestL"
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 200
        response_body = response.json()
        assert response_body["data"]["nModified"] == 1
        assert response_body["data"]["updatedExisting"] is True

    def test_check_change_pwd_with_middle_length_new_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": "123456&New"
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )
        assert response.status_code == 200
        response_body = response.json()
        assert response_body["data"]["nModified"] == 1
        assert response_body["data"]["updatedExisting"] is True

    def test_check_invalid_login_with_old_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        data = {
            "old_password": get_auth_user.password,
            "new_password": "123456New"
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )
        assert response.status_code == 200
        data_for_login = {
            "username": get_auth_user.username,
            "password": get_auth_user.password
        }
        response_login = auth.login(
            path=AuthUrls.LOGIN,
            data=data_for_login
        )

        assert response_login.status_code == 400
        response_login_body = response_login.json()
        current_msg = response_login_body["errors"]["login"]
        assert current_msg == UserAuthErrors.LOGIN_DOES_NOT_EXIST

    def test_check_valid_login_with_new_pwd(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        new_pwd = "NewTest_pwd&12"
        data = {
            "old_password": get_auth_user.password,
            "new_password": new_pwd
        }
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=data,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )
        assert response.status_code == 200

        data_for_login = {
            "username": get_auth_user.username,
            "password": new_pwd
        }

        response_for_login = auth.login(
            path=AuthUrls.LOGIN,
            data=data_for_login
        )

        assert response_for_login.status_code == 200
        resp_login_body = response_for_login.json()
        assert resp_login_body["errors"] is None
        assert resp_login_body["data"]["username"] == get_auth_user.username
