import requests

PATH = r"https://httpbin.org/post"

data = {
    "question": "什么是SQL注入?",
    "model": "kimi-k2"
}

headers = {
    "Authorization": "Bearer sk-fake-key-12345"
}

response = requests.post(PATH, headers=headers, json=data)
response_data = response.json()

if response.status_code == 200:
    print(response.status_code)
    print(response_data)
    print(response_data["json"])
    print(response_data["headers"]["Authorization"])
