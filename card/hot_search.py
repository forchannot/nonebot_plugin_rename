import random
import requests

URL = {
    "1": "https://tenapi.cn/v2/bilihot/",  # B站
    "2": "https://tenapi.cn/v2/weibohot",  # 微博
    "3": "https://tenapi.cn/v2/douyinhot",  # 抖音
    "4": "https://tenapi.cn/v2/baiduhot/",  # 百度
    "5": "https://tenapi.cn/v2/zhihuhot",  # 知乎
    "6": "https://tenapi.cn/v2/toutiaohot",  # 今日头条
}


def hot_search(num):
    res = requests.get(URL[str(num)])
    if res.status_code != 200:
        return "热搜api失效"
    result = res.json()["data"][random.choice([i for i in range(10)])]["name"]
    if len(result) <= 16:
        return result
    else:
        result = result[:16]
        return result
