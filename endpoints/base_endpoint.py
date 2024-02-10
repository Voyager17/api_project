from typing import Optional, Dict, Any

import allure
import requests
from pydantic import BaseModel, ValidationError


class BaseEndpoint:
    url: str = "http://167.172.172.115:52355/"
    response: Optional[requests.Response] = None
    json: Optional[Dict[str, Any]] = None
    token: str = "MfdeIjJkj0yzSqY"
    headers: Dict[str, str] = {
        "Content-type": "application/json",
        "Authorization": token,
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
    @allure.step("Update token")
    def update_token(cls, token: str) -> None:
        """
        Use this carefully because it changes value for base class and for all children
        """

        cls.token = token
        cls.headers["Authorization"] = f"{token}"

    @allure.step("Check life of selected token")
    def check_life_of_your_token(self, headers=None) -> None:
        self.response = requests.get(
            f"{self.url}authorize/{self.token}",
            headers=headers if headers else self.headers,
        )
        self.validate_status_code_is_200(error_message="Token is dead")

    @allure.step("Validate that status code is 200")
    def validate_status_code_is_200(
        self, error_message="Status code isn't 200"
    ) -> None:
        assert self.response.status_code == 200, error_message

    @allure.step("Validate that meme exists")
    def validate_meme_existing(self, meme_id) -> None:
        self.response = requests.get(
            f"{self.url}meme/{meme_id}",
            headers=self.headers,
        )
        self.validate_status_code_is_200(error_message="Mem is absent")

    @allure.step("Validate that message about deleting has come")
    def validate_message_about_deleting(self, meme_id) -> None:
        assert (
            f"Meme with id {meme_id} successfully deleted"
            in self.response.content.decode()
        ), "Meme wasn't deleted"

    @allure.step("Validate that meme is absent")
    def validate_meme_is_absent(self, meme_id) -> None:
        self.response = requests.get(
            f"{self.url}meme/{meme_id}",
            headers=self.headers,
        )
        assert self.response.status_code == 404, "Meme is still living"

    @allure.step("Validate changes for put request")
    def validate_put_changes(self, data, meme_id) -> None:
        self.response = requests.get(
            f"{self.url}meme/{meme_id}",
            headers=self.headers,
        )
        assert (
            meme_id == int(self.response.json()["id"])
            and data["text"] == self.response.json()["text"]
        ), "Not all information was updated"
