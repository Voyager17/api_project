from typing import Optional, Dict, Any

import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from models.put_meme_by_id_model import PutRequestModel


class PutMemeById(BaseEndpoint):
    def create_put_meme_by_id(
        self,
        payload: Dict[str, Any],
        meme_id: str,
        headers: Optional[Dict[str, str]] = None,
    ) -> requests.Response:
        with allure.step("Validate request data according to a model"):
            validated_payload = PutRequestModel(**payload).model_dump()

        self.response = requests.put(
            f"{self.url}meme/{meme_id}",
            json=validated_payload,
            headers=headers if headers else self.headers,
        )
        self.json = self.response.json()
        return self.response
