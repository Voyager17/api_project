from typing import Optional, Dict, Any

import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from models.post_authorize_model import PostRequestModel


class PostAuthorization(BaseEndpoint):
    def create_post_authorization(
        self, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None
    ) -> requests.Response:
        with allure.step("Validate request data according to a model"):
            validated_payload = PostRequestModel(**payload).model_dump()

        with allure.step("Creating a Post request"):
            self.response = requests.post(
                f"{self.url}authorize",
                json=validated_payload,
                headers=headers if headers else self.headers,
            )

        self.json = self.response.json()
        return self.response

    @staticmethod
    def update_parent_token(new_token: str) -> None:
        BaseEndpoint.update_token(new_token)
