import requests

from endpoints.base_endpoint import BaseEndpoint


class GetMeme(BaseEndpoint):
    def create_get_meme(self, headers=None):
        self.response = requests.get(
            f"{self.url}meme",
            headers=headers if headers else self.headers,
        )
        self.json = self.response.json()
        return self.response
