import requests

from endpoints.base_endpoint import BaseEndpoint


class GetAuthorizationToken(BaseEndpoint):
    def create_get_authorize_token(self, headers=None):
        self.response = requests.get(
            f"{self.url}authorize/{self.token}",
            headers=headers if headers else self.headers,
        )
        return self.response
