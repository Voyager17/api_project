import allure

from endpoints.delete_meme_by_id import DeleteMemeById


@allure.feature("Common user's actions")
@allure.story("Send a valid Delete_meme request")
@allure.title("Test for a DELETE request")
def test_delete_meme_by_id(
    delete_meme_by_id_endpoint: DeleteMemeById, create_a_meme_and_get_id: str
) -> None:
    meme_id = create_a_meme_and_get_id
    delete_meme_by_id_endpoint.create_delete_meme_by_id(meme_id)
    delete_meme_by_id_endpoint.validate_message_about_deleting(meme_id)
    delete_meme_by_id_endpoint.validate_meme_is_absent(meme_id)
