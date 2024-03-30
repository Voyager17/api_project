import allure
import pytest

from endpoints.get_meme import GetMeme
from models.get_meme_model import ResponseDataModel


@pytest.mark.smoke
@allure.feature("Common user's actions")
@allure.story("Send a valid Get_Meme request")
@allure.title("Test for a Get_Meme request")
def test_get_meme(get_meme_endpoint: GetMeme) -> None:
    get_meme_endpoint.create_get_meme()
    get_meme_endpoint.validate_response(ResponseDataModel)
    get_meme_endpoint.validate_status_code_is_200()
