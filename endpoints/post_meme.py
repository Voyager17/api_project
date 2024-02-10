from typing import Optional, Dict, Any

import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from models.post_meme_model import PostRequestModel


class PostMeme(BaseEndpoint):
    def create_post_meme(
        self, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        with allure.step("Validate request data according to a model"):
            validated_payload = PostRequestModel(**payload).model_dump()

        self.response = requests.post(
            f"{self.url}meme",
            json=validated_payload,
            headers=headers if headers else self.headers,
        )
        self.json = self.response.json()
        return self.response
