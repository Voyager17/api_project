def test_get_authorize_token(get_authorize_token_endpoint):
    get_authorize_token_endpoint.create_get_authorize_token()
    get_authorize_token_endpoint.validate_status_code_is_200()
