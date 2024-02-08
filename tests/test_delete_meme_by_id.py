def test_delete_meme_by_id(delete_meme_by_id_endpoint, create_a_meme_and_get_id):
    meme_id = create_a_meme_and_get_id
    delete_meme_by_id_endpoint.create_delete_meme_by_id(meme_id)
    delete_meme_by_id_endpoint.validate_message_about_deleting(meme_id)
    delete_meme_by_id_endpoint.validate_meme_is_absent(meme_id)
