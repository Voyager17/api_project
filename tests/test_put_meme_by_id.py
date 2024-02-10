import allure

from endpoints.put_meme_by_id import PutMemeById
from models.put_meme_by_id_model import PutResponseModel


@allure.feature("Common user's actions")
@allure.story("Send a valid Put_Meme request")
@allure.title("Test for a Put_Meme request")
def test_put_meme_by_id(
    put_meme_by_id_endpoint: PutMemeById, create_a_meme_and_get_id: str
) -> None:
    meme_id = create_a_meme_and_get_id

    data = {
        "id": meme_id,
        "text": "PUT Unhappy dogge",
        "url": "https://www.funnyart.club/uploads/posts"
        "/2023-02/1675281995_www-funnyart-club-p-khatiko-mem-shutki-61.jpg",
        "tags": ["fixture", "dogge", "changed"],
        "info": {
            "colors": ["black", "orange", "yellow"],
            "objects": ["picture", "no text"],
        },
    }
    put_meme_by_id_endpoint.create_put_meme_by_id(payload=data, meme_id=meme_id)
    put_meme_by_id_endpoint.validate_response(PutResponseModel)
    put_meme_by_id_endpoint.validate_put_changes(meme_id=meme_id, data=data)
