from tests.tests_api.api_helpers.auth import ApiAuth
from tests.tests_api.constants import AuthUrls


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
        print(response)
        assert response.status_code == 400

    def test_check_change_pwd_without_old_pwd(self):
        pass

    def test_check_change_pwd_without_new_pwd(self):
        pass

    def test_check_change_pwd_with_empty_fields(self):
        pass

    def test_check_change_pwd_with_empty_old_pwd(self):
        pass

    def test_check_change_pwd_with_empty_new_pwd(self):
        pass

    def test_check_change_pwd_with_invalid_old_pwd(self):
        pass

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
