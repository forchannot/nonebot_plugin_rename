# Description: 获取热搜

import random

import httpx
from nonebot import logger

from ..config import env_config

URL1 = {
    "1": ("bilibili", "B站"),  # B站
    "2": ("weibo", "微博"),  # 微博
    "3": ("newsqq", "腾讯"),  # 腾讯新闻
    "4": ("baidu", "百度"),  # 百度
    "5": ("zhihu", "知乎"),  # 知乎
    "6": ("toutiao", "头条"),  # 今日头条
}  # hot.zhenxun.buzz
URL2 = {
    "1": ("bilihot", "B站"),  # B站
    "2": ("weibohot", "微博"),  # 微博
    "3": ("douyinhot", "抖音"),  # 抖音
    "4": ("baiduhot", "百度"),  # 百度
    "5": ("zhihuhot", "知乎"),  # 知乎
    "6": ("toutiaohot", "头条"),  # 今日头条
}  # tenapi.cn


async def hot(num: int) -> str:
    URLSTART = (
        "https://hot.zhenxun.buzz"
        if env_config.hot_search_url == 1
        else "https://tenapi.cn/v2"
    )
    URL = URL1 if env_config.hot_search_url == 1 else URL2
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            res = await client.get(f"{URLSTART}/{URL[str(num)][0]}")
            if res.status_code != 200:
                logger.warning(
                    f"获取{URL[str(num)][1]}热搜失败: {res.status_code}，请尝试更换API后重启"
                )
                return "热搜获取失败"
            data = res.json()["data"]
            result = (
                random.choice(data)["title"]
                if env_config.hot_search_url == 1
                else random.choice(data)["name"]
            )
            if env_config.is_show_hot_search_from:
                result = f"{URL[str(num)][1]}：{result}"
            return result
        except Exception as e:
            logger.warning(f"获取热搜{URL[str(num)][1]}失败: {e}，请尝试更换API后重启")
            return "热搜获取失败"
