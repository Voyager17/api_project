def test_post_meme(post_meme_endpoint, delete_meme_by_id_endpoint):
    data = {
        "text": "Sad dogge",
        "url": "https://www.funnyart.club/uploads/posts"
        "/2023-02/1675281995_www-funnyart-club-p-khatiko-mem-shutki-61.jpg",
        "tags": ["sad", "dogge"],
        "info": {
            "colors": ["black", "orange", "yellow"],
            "objects": ["picture", "no text"],
        },
    }

    post_meme_endpoint.create_post_meme(payload=data)
    meme_id = post_meme_endpoint.json["id"]
    post_meme_endpoint.validate_meme_existing(meme_id)
    delete_meme_by_id_endpoint.create_delete_meme_by_id(meme_id)