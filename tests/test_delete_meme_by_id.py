import allure
import pytest

from endpoints.delete_meme_by_id import DeleteMemeById


@pytest.mark.regression
@allure.feature("Common user's actions")
@allure.story("Send a valid Delete_meme request")
@allure.title("Test for a DELETE request")
def test_delete_meme_by_id(
    delete_meme_by_id_endpoint: DeleteMemeById, create_a_meme_and_get_id: str
) -> None:
    """
    1. Create a meme and save its id
    2. Delete meme by id
    3. Validate message about successful deleting
    4. Validate that meme is absent
    """

    meme_id = create_a_meme_and_get_id
    delete_meme_by_id_endpoint.create_delete_meme_by_id(meme_id)
    delete_meme_by_id_endpoint.validate_message_about_deleting(meme_id)
    delete_meme_by_id_endpoint.validate_meme_is_absent(meme_id)
