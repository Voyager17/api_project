def test_get_authorize_token(create_get_authorize_token):
    create_get_authorize_token.create_get_authorize_token()
    create_get_authorize_token.validate_status_code_is_200()
