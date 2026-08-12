import os
from abc_api_client import request_api

api_key = os.getenv("DeepSeek_API_KEY")
if not api_key:
    print("没有读取到环境变量")
    raise SystemExit

URL = r"https://api.deepseek.com/chat/completions"


def talk_with_ai(model, api_key, url):

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是一位网络安全老师，用大白话向大一学生讲解概念，多举生活例子"}
        ]
    }

    while True:

        question = input("你:")
        question = question.strip()
        if question == "q":
            print("对话结束")
            break

        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        data["messages"].append({
            "role": "user",
            "content": question
        })

        result = request_api("post", url, headers=headers, json_data=data, timeout=30)

        if result["message"] is None and result["success"]:
            response = result["data"]["choices"][0]["message"]["content"]

            print("", response)

            data["messages"].append({
                "role": "assistant",
                "content": response
            })

        else:
            print("对话异常，请尝试重新输入...也可以输入q退出对话")
            data["messages"].pop()  # 撤销悬空的 user 消息，保持历史干净
            continue


talk_with_ai("deepseek-v4-flash", api_key, URL)
