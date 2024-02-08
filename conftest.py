import pytest

from endpoints.base_endpoint import BaseEndpoint
from endpoints.get_authorize_token import GetAuthorizationToken
from endpoints.post_authorize import PostAuthorization


@pytest.fixture()
def create_post_authorization() -> PostAuthorization:
    return PostAuthorization()


@pytest.fixture()
def create_get_authorize_token() -> GetAuthorizationToken:
    return GetAuthorizationToken()


@pytest.fixture(scope="session", autouse=True)
def get_token_and_updated_headers(check_life_of_the_token):
    data = {"name": "texxtim"}
    if not check_life_of_the_token:
        new_post = PostAuthorization()
        new_post.create_post_authorization(payload=data)
        # new.post.update_token doesn't update base endpoint
        BaseEndpoint.update_token(new_post.json["token"])


@pytest.fixture(scope="session")
def check_life_of_the_token():
    new_get = GetAuthorizationToken()
    new_get.create_get_authorize_token()
    return True if new_get.response.status_code == 200 else False
