import requests

from endpoints.base_endpoint import BaseEndpoint


class DeleteMemeById(BaseEndpoint):
    def create_delete_meme_by_id(self, meme_id: str, headers=None):
        self.response = requests.delete(
            f"{self.url}meme/{meme_id}",
            headers=headers if headers else self.headers,
        )
        return self.response
