from tests.tests_api.api_helpers.auth import ApiAuth
from tests.tests_api.constants import AuthUrls
from tests.tests_api.data.messages import UserAuthErrors


class TestUnsuccessfulDeleteUser:
    def test_check_delete_user_without_cookie(
            self,
            base_url,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        response = auth.delete_user(
            path=AuthUrls.DELETE,
            headers=get_auth_user.headers,
            cookies=None
        )
        assert response.status_code == 401
        response_body = response.json()
        current_msg = response_body["msg"]
        assert current_msg == UserAuthErrors.MISSING_COOKIE_ACCESS_TOKEN

    def test_check_delete_user_without_xcsrf_token(
            self,
            base_url,
            get_base_header,
            get_auth_user
    ):
        auth = ApiAuth(base_url=base_url)
        response = auth.delete_user(
            path=AuthUrls.DELETE,
            headers=get_base_header,
            cookies=get_auth_user.cookie
        )

        assert response.status_code == 401
        response_body = response.json()
        current_msg = response_body["msg"]
        assert current_msg == UserAuthErrors.MISSING_CSRF_TOKEN

    def test_check_delete_user_with_invalid_token(
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

        response = auth.delete_user(
            path=AuthUrls.DELETE,
            headers=my_headers,
            cookies=cookie
        )
        assert response.status_code == 401
        response_body = response.json()
        current_message = response_body["msg"]
        assert current_message == UserAuthErrors.INVALID_CSRF_TOKEN

    def test_check_delete_user_with_invalid_cookie(
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
        response = auth.delete_user(
            path=AuthUrls.DELETE,
            headers=get_auth_user.headers,
            cookies=my_cookie
        )
        assert response.status_code == 422
        response_body = response.json()
        current_message = response_body["msg"]
        assert current_message == UserAuthErrors.INVALID_TOKEN_IN_COOKIE


class TestSuccessfulDeleteUser:
    def test_check_delete_user(
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
        response_body = response.json()
        current_msg = response_body["data"]["delete"]
        assert current_msg == "ok"

