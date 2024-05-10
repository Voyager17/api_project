import allure
import pytest

from endpoints.get_meme_by_id import GetMemeById
from models.get_meme_by_id_model import ResponseDataModel


@pytest.mark.simple
@allure.feature("Common user's actions")
@allure.story("Send a valid Get_Meme_By_Id request")
@allure.title("Test for a Get_Meme_By_Id request")
def test_get_meme_by_id(
    get_meme_by_id_endpoint: GetMemeById, create_a_meme_and_get_id: str
) -> None:
    """
    1. Create a meme and save its id by a fixture
    2. Get a meme by id
    3. Validate a response model
    4. Validate a status code
    """
    get_meme_by_id_endpoint.create_get_meme_by_id(create_a_meme_and_get_id)
    get_meme_by_id_endpoint.validate_response(ResponseDataModel)
    get_meme_by_id_endpoint.validate_status_code_is_200()
