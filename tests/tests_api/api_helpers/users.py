import requests

from tests.tests_api.api_helpers.base import ApiBase
from tests.tests_api.constants import UsersUrls


class ApiUsers(ApiBase):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.users_route = UsersUrls.USERS_API

    def get_profile_info(
            self,
            path="",
            params=None,
            headers=None,
            cookies=None
    ):
        url = f"{self.base_url}{self.users_route}{path}"
        return requests.get(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies
        )
