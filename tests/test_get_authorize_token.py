import allure

from endpoints.get_authorize_token import GetAuthorizationToken


@allure.feature("Common user's actions")
@allure.story("Send a valid Get_Authorize request")
@allure.title("Test for a Get_Authorize request")
def test_get_authorize_token(
    get_authorize_token_endpoint: GetAuthorizationToken,
) -> None:
    get_authorize_token_endpoint.create_get_authorize_token()
    get_authorize_token_endpoint.validate_status_code_is_200()
