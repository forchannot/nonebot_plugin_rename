# Description: 获取热搜

import random

import httpx
from nonebot import logger

from ..config import env_config

# URL = {
#     "1": "https://tenapi.cn/v2/bilihot/",  # B站
#     "2": "https://tenapi.cn/v2/weibohot",  # 微博
#     "3": "https://tenapi.cn/v2/douyinhot",  # 抖音
#     "4": "https://tenapi.cn/v2/baiduhot/",  # 百度
#     "5": "https://tenapi.cn/v2/zhihuhot",  # 知乎
#     "6": "https://tenapi.cn/v2/toutiaohot",  # 今日头条
# }
URL = {
    "1": ("bilibili", "B站"),  # B站
    "2": ("weibo", "微博"),  # 微博
    "3": ("newsqq", "腾讯"),  # 腾讯新闻
    "4": ("baidu", "百度"),  # 百度
    "5": ("zhihu", "知乎"),  # 知乎
    "6": ("toutiao", "头条"),  # 今日头条
}


async def hot(num: int) -> str:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            res = await client.get(f"https://hot.zhenxun.buzz/{URL[str(num)][0]}")
            data = res.json()["data"]
            result = random.choice(data)["title"]
            if env_config.is_show_hot_search_from:
                result = f"{URL[str(num)][1]}：{result}"
            return result
        except Exception as e:
            logger.warning(f"获取热搜失败: {e}")
            return "热搜获取失败"
