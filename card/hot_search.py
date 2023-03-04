import requests

URL = {
    "1": "https://tenapi.cn/v2/bilihot/",  # B站
    "2": "https://tenapi.cn/v2/weibohot",  # 微博
    "3": "https://tenapi.cn/v2/douyinhot",  # 抖音
    "4": "https://tenapi.cn/v2/baiduhot/",  # 百度
    "5": "https://tenapi.cn/v2/zhihuhot",  # 知乎
    "6": "https://tenapi.cn/v2/toutiaohot",  # 头条
}


def hot_search(num):
    res = requests.get(URL[str(num)])
    if res.status_code != 200:
        return False
    for i in range(0, len(res.json()["data"]) + 1):
        result = res.json()["data"][i]["name"]
        if len(result) <= 16:
            return result
        else:
            result = result[:16]
            return result
