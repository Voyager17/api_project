def test_get_meme_by_id(get_meme_by_id_endpoint, create_a_meme_and_get_id):
    get_meme_by_id_endpoint.create_get_meme_by_id(create_a_meme_and_get_id)
    get_meme_by_id_endpoint.validate_status_code_is_200()
