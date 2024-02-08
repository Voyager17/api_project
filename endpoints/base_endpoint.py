from typing import Optional, Dict, Any

import allure
import requests
from pydantic import BaseModel, ValidationError


class BaseEndpoint:
    url: str = "http://167.172.172.115:52355/"
    response: Optional[requests.Response] = None
    json: Optional[Dict[str, Any]] = None
    token: str = "1"
    headers: Dict[str, str] = {
        "Content-type": "application/json",
        "Authorization": "pbZMiJTqDZKE2LD",
    }

    @allure.step("Validate response data according to a model")
    def validate_response(self, response_model: type[BaseModel]) -> None:
        if self.json is None:
            raise AssertionError("No data in JSON.")
        try:
            response_model.model_validate(self.json)
        except ValidationError as e:
            raise AssertionError(f"Validation error: {e}")

    @classmethod
    def update_token(cls, token: str) -> None:
        """
        Use this carefully because it changes value for base class and for all children
        """

        cls.token = token
        cls.headers["Authorization"] = f"{token}"

    def check_life_of_your_token(self, headers=None) -> None:
        self.response = requests.get(
            f"{self.url}/authorize/{self.token}",
            headers=headers if headers else self.headers,
        )
        self.validate_status_code_is_200(error_message="Token is dead")

    def validate_status_code_is_200(
        self, error_message="Status code isn't 200"
    ) -> None:
        assert self.response.status_code == 200, error_message
