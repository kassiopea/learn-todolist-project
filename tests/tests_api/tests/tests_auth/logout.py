from tests.tests_api.api_helpers.auth import ApiAuth
from tests.tests_api.api_helpers.users import ApiUsers
from tests.tests_api.constants import AuthUrls, UsersUrls
from tests.tests_api.data.messages import UserAuthErrors, UserAuthMessages


class TestInvalidLogout:
    def test_check_invalid_logout_without_cookie_access_token(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        response = auth.logout(
            path=AuthUrls.LOGOUT,
            headers=get_auth_user.headers,
            cookies=None
        )
        assert response.status_code == 401
        response_body = response.json()
        current_message = response_body["msg"]
        assert current_message == UserAuthErrors.MISSING_COOKIE_ACCESS_TOKEN

    def test_check_invalid_logout_without_xscrf_token(
            self,
            base_url,
            get_base_header,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        response = auth.logout(
            path=AuthUrls.LOGOUT,
            headers=get_base_header,
            cookies=get_auth_user.cookie
        )
        assert response.status_code == 401
        response_body = response.json()
        current_message = response_body["msg"]
        assert current_message == UserAuthErrors.MISSING_CSRF_TOKEN

    def test_check_invalid_logout_with_invalid_cookie(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        cookie = get_auth_user.cookie
        my_cookie = {
            "access_token": f'{cookie["access_token"]}!',
            "csrf_access_token": cookie["csrf_access_token"]
        }

        response = auth.logout(
            path=AuthUrls.LOGOUT,
            headers=get_auth_user.headers,
            cookies=my_cookie
        )

        assert response.status_code == 422
        response_body = response.json()
        current_message = response_body["msg"]
        assert current_message == UserAuthErrors.INVALID_TOKEN_IN_COOKIE

    def test_check_invalid_logout_with_invalid_xscrf_token(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        cookie = get_auth_user.cookie
        my_cookie = {
            "access_token": cookie["access_token"],
            "csrf_access_token": f'{cookie["csrf_access_token"]}!'
        }
        my_headers = get_auth_user.headers
        my_headers["X-CSRF-TOKEN-ACCESS"] = f'{cookie["csrf_access_token"]}!'

        response = auth.logout(
            path=AuthUrls.LOGOUT,
            headers=my_headers,
            cookies=my_cookie
        )

        assert response.status_code == 401
        response_body = response.json()
        current_message = response_body["msg"]
        assert current_message == UserAuthErrors.INVALID_CSRF_TOKEN


class TestValidLogout:
    def test_check_logout(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        response = auth.logout(
            path=AuthUrls.LOGOUT,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 200
        response_body = response.json()
        assert response_body["errors"] is None
        current_message = response_body["data"]
        assert current_message == UserAuthMessages.REVOKED_TOKEN

    def test_check_expired_token(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        response = auth.logout(
            path=AuthUrls.LOGOUT,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )
        assert response.status_code == 200

        users = ApiUsers(base_url=base_url)
        response_get_info = users.get_profile_info(
            path=UsersUrls.PROFILE,
            headers=get_auth_user.headers,
            cookies=get_auth_user.cookie
        )

        assert response_get_info.status_code == 401
        response_get_info_body = response_get_info.json()
        current_message = response_get_info_body["msg"]
        assert current_message == UserAuthErrors.REVOKED_TOKEN
