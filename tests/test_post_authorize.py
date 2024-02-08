def test_post_authorize(create_post_authorization):
    data = {"name": "timteex"}
    headers = {"Content-type": "application/json"}
    create_post_authorization.create_post_authorization(payload=data, headers=headers)
    create_post_authorization.check_life_of_your_token()
