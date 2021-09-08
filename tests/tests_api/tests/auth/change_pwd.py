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
            json_empty_change_pwd
    ):
        auth = ApiAuth(base_url=base_url)
        response = auth.change_password(
            path=AuthUrls.CHANGE_PASSWORD,
            data=json_empty_change_pwd,
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
        print(response_body)
        current_msg = response_body["errors"][0]["old_password"]
        assert current_msg == UserAuthErrors.INCORRECT_PASSWORD

    def test_check_change_pwd_with_invalid_new_pwd(self):
        pass

    def test_check_change_pwd_with_equal_new_and_old_pws(self):
        pass

    def test_check_change_pwd_without_cookie(self):
        pass

    def test_check_change_pwd_without_xcsrf_token_in_headers(self):
        pass


class TestSuccessfulPasswordChange:
    def test_check_change_pwd_with_min_length_new_pwd(self):
        pass

    def test_check_change_pwd_with_max_length_new_pwd(self):
        pass

    def test_check_change_pwd_with_middle_length_new_pwd(self):
        pass
