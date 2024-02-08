def test_get_meme(get_meme_endpoint):
    get_meme_endpoint.create_get_meme()
    get_meme_endpoint.validate_status_code_is_200()
