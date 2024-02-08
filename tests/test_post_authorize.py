def test_post_authorize(post_authorization_endpoint):
    data = {"name": "timteex"}
    headers = {"Content-type": "application/json"}
    post_authorization_endpoint.create_post_authorization(payload=data, headers=headers)
    post_authorization_endpoint.check_life_of_your_token()
