import requests

from endpoints.base_endpoint import BaseEndpoint


class PutMemeById(BaseEndpoint):
    def create_put_meme_by_id(self, payload: dict, meme_id: str, headers=None):
        self.response = requests.put(
            f"{self.url}meme/{meme_id}",
            json=payload,
            headers=headers if headers else self.headers,
        )
        return self.response
