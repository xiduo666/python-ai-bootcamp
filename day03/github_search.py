import requests

params = {
    "q": "security",
    "per_page": 5
}
response = requests.get("https://api.github.com/search/repositories", params=params)

response_data = response.json()

# 铁律：先查状态码再解析
if response.status_code != 200:
    print(f"请求失败，状态码{response.status_code}")
    print(response_data.get("message", "无详细信息"))
else:
    for data in response_data["items"]:
        data_name = data["name"]
        data_stargazers_count = data["stargazers_count"]
        data_html_url = data["html_url"]

        print(f"{data_name} | {data_stargazers_count} | {data_html_url}")
