import requests
import os

URL = r"https://api.deepseek.com/chat/completions"
api_key = os.getenv("DeepSeek_API_KEY")
if not api_key:
    print("没有读取到环境变量")
    raise SystemExit

headers = {
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "deepseek-v4-flash",
    "messages": [
        {
            "role": "user",
            "content": "评价一下chatGPT?"
        }
    ]
}

try:
    response = requests.post(URL, headers=headers, json=data, timeout=30)

    response.raise_for_status()

    response_data = response.json()

    print("User:", data["messages"][0]["content"])
    print(response_data["model"], ":", response_data["choices"][0]["message"]["content"])

except requests.exceptions.Timeout as e:
    print(f"请求超时:{e}")

except requests.exceptions.ConnectionError as e:
    print(f"网络断开:{e}")

except requests.exceptions.HTTPError as e:
    print(f"HTTP错误:{e}")

except requests.exceptions.JSONDecodeError as e:
    print(f"JSON解析错误:{e}")

except requests.exceptions.RequestException as e:
    print(f"请求错误:{e}")
