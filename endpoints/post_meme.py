import requests

from endpoints.base_endpoint import BaseEndpoint


class PostMeme(BaseEndpoint):
    def create_post_meme(self, payload, headers=None):
        self.response = requests.post(
            f"{self.url}meme",
            json=payload,
            headers=headers if headers else self.headers,
        )
        self.json = self.response.json()
        return self.response
