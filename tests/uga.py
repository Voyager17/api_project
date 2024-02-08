import requests

# data = {"name": "texxtim"}
# headers = {"Content-type": "application/json", "Authorization": "pbZMiJTqDZKE2LD"}
# response = requests.post(
# f"http://167.172.172.115:52355/authorize/pbZMiJTqDZKE2LD", headers=headers
# )
# print(response)

data = {"name": "texxtim"}
headers = {"Content-type": "application/json"}
response = requests.get(
    f"http://167.172.172.115:52355/authorize/pbZMiJTqDZKE2LD", headers=headers
)
print(response.content)

data2 = {"name": "texxtim"}
headers2 = {"Content-type": "application/json"}
response = requests.post(
    f"http://167.172.172.115:52355/authorize",
    "texxtim1",
    headers=headers2,
)
print(response.content)
