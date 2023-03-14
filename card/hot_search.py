import random
import httpx

URL = {
    "1": "https://tenapi.cn/v2/bilihot/",  # B站
    "2": "https://tenapi.cn/v2/weibohot",  # 微博
    "3": "https://tenapi.cn/v2/douyinhot",  # 抖音
    "4": "https://tenapi.cn/v2/baiduhot/",  # 百度
    "5": "https://tenapi.cn/v2/zhihuhot",  # 知乎
    "6": "https://tenapi.cn/v2/toutiaohot",  # 今日头条
}


async def hot(num: int) -> str:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        res = await client.get(URL[str(num)])
        if res.status_code != 200:
            return "热搜api失效"
        data = res.json()['data']
        result = random.choice(data)['name']
        return result[:16]
