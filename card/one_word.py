import requests


def get_one_speak():
    res = requests.get("https://tenapi.cn/v2/yiyan?format=json").json()["data"][
        "hitokoto"
    ]
    return res
