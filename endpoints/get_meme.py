from typing import Optional, Dict

import requests

from endpoints.base_endpoint import BaseEndpoint


class GetMeme(BaseEndpoint):
    def create_get_meme(
        self, headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        self.response = requests.get(
            f"{self.url}meme",
            headers=headers if headers else self.headers,
        )
        self.json = self.response.json()
        return self.response
