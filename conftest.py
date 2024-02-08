import pytest

from endpoints.delete_meme_by_id import DeleteMemeById
from endpoints.get_authorize_token import GetAuthorizationToken
from endpoints.get_meme import GetMeme
from endpoints.get_meme_by_id import GetMemeById
from endpoints.post_authorize import PostAuthorization
from endpoints.post_meme import PostMeme
from endpoints.put_meme_by_id import PutMemeById


@pytest.fixture()
def post_authorization_endpoint() -> PostAuthorization:
    return PostAuthorization()


@pytest.fixture()
def get_authorize_token_endpoint() -> GetAuthorizationToken:
    return GetAuthorizationToken()


@pytest.fixture()
def get_meme_endpoint() -> GetMeme:
    return GetMeme()


@pytest.fixture()
def post_meme_endpoint() -> PostMeme:
    return PostMeme()


@pytest.fixture()
def get_meme_by_id_endpoint() -> GetMemeById:
    return GetMemeById()


@pytest.fixture()
def delete_meme_by_id_endpoint() -> DeleteMemeById:
    return DeleteMemeById()


@pytest.fixture()
def put_meme_by_id_endpoint() -> PutMemeById:
    return PutMemeById()


@pytest.fixture()
def create_a_meme_and_get_id(post_meme_endpoint, delete_meme_by_id_endpoint):
    data = {
        "text": "Unhappy dogge",
        "url": "https://www.funnyart.club/uploads/posts"
        "/2023-02/1675281995_www-funnyart-club-p-khatiko-mem-shutki-61.jpg",
        "tags": ["fixture", "dogge"],
        "info": {
            "colors": ["black", "orange", "yellow"],
            "objects": ["picture", "no text"],
        },
    }
    post_meme_endpoint.create_post_meme(payload=data)
    yield post_meme_endpoint.json["id"]
    delete_meme_by_id_endpoint.create_delete_meme_by_id(post_meme_endpoint.json["id"])


@pytest.fixture(scope="session", autouse=True)
def get_token_and_updated_headers(check_life_of_the_token):
    data = {"name": "texxtim"}
    if not check_life_of_the_token:
        new_post = PostAuthorization()
        new_post.create_post_authorization(payload=data)
        new_post.update_parent_token(new_post.json["token"])


@pytest.fixture(scope="session")
def check_life_of_the_token():
    new_get = GetAuthorizationToken()
    new_get.create_get_authorize_token()
    return True if new_get.response.status_code == 200 else False
