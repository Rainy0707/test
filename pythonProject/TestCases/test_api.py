import requests
from requests.structures import CaseInsensitiveDict

# def test_api():
data = {
"email": "eve.holt@reqres.in",
"password": "cityslicka"
}
resp = requests.post("https://reqres.in/api/login", data = data)
print(resp.text)
# assert resp.status_code ==200, "Response doesn't match"
token = resp.text
headers = CaseInsensitiveDict()

headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer {token}"

resp = requests.get(url, headers=headers)

print(resp.status_code)
