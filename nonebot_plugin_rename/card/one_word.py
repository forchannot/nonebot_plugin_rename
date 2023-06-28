# Description: 获取一言


import httpx
from nonebot import logger


async def get_one_speak() -> str:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            res = await client.get("https://v1.hitokoto.cn/")
            if res.status_code != 200:
                logger.warning(f"获取一言失败: {res.status_code}")
                return "一言获取失败"
            data = res.json()["hitokoto"]
            return data[:16]
        except Exception as e:
            logger.warning(f"获取一言失败: {e}")
            return "一言获取失败"
