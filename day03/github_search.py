import requests


def search_github(keyword, count):
    params = {
        "q": keyword,
        "per_page": count
    }

    response = requests.get("https://api.github.com/search/repositories", params=params)

    response_data = response.json()

    if response.status_code != 200:
        return {
            "success": False,
            "status_code": response.status_code,
            "message": response_data.get("message", "无详细信息"),
            "data": []
        }

    return {
        "success": True,
        "status_code": response.status_code,
        "message": "",
        "data": [
            {
                "name": data["name"],
                "stargazers_count": data["stargazers_count"],
                "html_url": data["html_url"]
            }
            for data in response_data["items"]
        ]
    }


result = search_github("security", 5)
print(result)
