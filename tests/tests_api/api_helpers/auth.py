import requests

from tests.tests_api.api_helpers.base import ApiBase
from tests.tests_api.constants import AuthUrls


class ApiAuth(ApiBase):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.auth_route = AuthUrls.AUTH

    def registration(
            self,
            path="",
            params=None,
            data=None,
            headers=None
    ):
        url = f"{self.base_url}{self.auth_route}{path}"
        return requests.post(
            url=url,
            params=params,
            data=data,
            headers=headers
        )

    def login(
            self,
            path="",
            params=None,
            data=None,
            headers=None
    ):
        url = f"{self.base_url}{self.auth_route}{path}"
        return requests.post(
            url=url,
            params=params,
            data=data,
            headers=headers
        )

    def change_password(
            self,
            path="",
            params=None,
            data=None,
            headers=None,
            cookie=None
    ):
        url = f"{self.base_url}{self.auth_route}{path}"
        return requests.put(
            url=url,
            params=params,
            data=data,
            headers=headers,
            cookies=cookie
        )

    def logout(
            self,
            path="",
            headers=None,
            cookies=None
    ):
        url = f"{self.base_url}{self.auth_route}{path}"
        return requests.delete(
            url=url,
            headers=headers,
            cookies=cookies
        )

    def delete_user(
            self,
            path="",
            headers=None,
            cookies=None
    ):
        url = f"{self.base_url}{self.auth_route}{path}"
        return requests.delete(
            url=url,
            headers=headers,
            cookies=cookies
        )

    # def get(self, path='', params=None, headers=None):
    #     url = f"{self.base_url}{path}"
    #     return requests.get(url=url, params=params, headers=headers)
    #
    # def delete(self, path='', headers=None):
    #     url = f"{self.base_url}{path}"
    #     return requests.delete(url=url, headers=headers)