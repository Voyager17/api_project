import requests

from endpoints.base_endpoint import BaseEndpoint


class PostAuthorization(BaseEndpoint):
    def create_post_authorization(self, payload, headers=None):
        self.response = requests.post(
            f"{self.url}authorize",
            json=payload,
            headers=headers if headers else self.headers,
        )
        self.json = self.response.json()
        return self.response

    @staticmethod
    def update_parent_token(new_token):
        BaseEndpoint.update_token(new_token)
