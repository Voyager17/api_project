import allure
import pytest

from endpoints.post_authorize import PostAuthorization
from models.post_authorize_model import PostResponseModel


@pytest.mark.smoke
@allure.feature("Common user's actions")
@allure.story("Send a valid Post_Authorize request")
@allure.title("Test for a Post_Authorize request")
def test_post_authorize(post_authorization_endpoint: PostAuthorization) -> None:
    """
    1. Make the authorization by post request
    2. Validate a response model
    3. Check that token is alife
    """

    data = {"name": "timteex"}
    headers = {"Content-type": "application/json"}

    post_authorization_endpoint.create_post_authorization(payload=data, headers=headers)
    post_authorization_endpoint.validate_response(PostResponseModel)
    post_authorization_endpoint.check_life_of_your_token()
