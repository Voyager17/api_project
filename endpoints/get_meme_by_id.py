from typing import Optional, Dict

import requests

from endpoints.base_endpoint import BaseEndpoint


class GetMemeById(BaseEndpoint):
    def create_get_meme_by_id(
        self, meme_id: str, headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        self.response = requests.get(
            f"{self.url}meme/{meme_id}",
            headers=headers if headers else self.headers,
        )
        self.json = self.response.json()
        return self.response
