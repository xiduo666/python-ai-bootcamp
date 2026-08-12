import requests


def request_api(method, url, headers=None, params=None, json_data=None, timeout=5):

    is_success = False
    no_response = False
    message = None  # 注意：= 赋值，不是 is 比较
    try:
        response = requests.request(method=method, url=url, headers=headers, params=params, json=json_data, timeout=timeout)

        response.raise_for_status()

        response_data = response.json()

        is_success = True

    except requests.exceptions.Timeout as e:
        no_response = True
        message = "请求超时"
        print(f"请求超时:{e}")

    except requests.exceptions.ConnectionError as e:
        no_response = True
        message = "网络连接错误"
        print(f"网络连接错误:{e}")

    except requests.exceptions.HTTPError as e:
        message = "HTTP错误"
        print(f"HTTP错误:{e}")

    except requests.exceptions.JSONDecodeError as e:
        message = "JSON解析错误"
        print(f"JSON解析错误:{e}")

    except requests.exceptions.RequestException as e:
        print(f"请求错误:{e}")

    return {
        "success": is_success,
        "status_code": response.status_code if not no_response else None,
        "message": message,
        "data": response_data if is_success and not no_response else None
    }
