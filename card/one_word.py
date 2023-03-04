import requests


def get_one_speak():
    res = requests.get("https://tenapi.cn/v2/yiyan?format=json").json()["data"][
        "hitokoto"
    ]
    if len(res) > 16:
        res = res[:16]
    return res
