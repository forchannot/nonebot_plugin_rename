# Description: 获取一言

import httpx
from nonebot import logger


async def get_one_speak() -> str | None:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            res = await client.get("https://v1.hitokoto.cn/")
            data = res.json()["hitokoto"]
            return data[:16]
        except Exception as e:
            logger.warning(f"获取一言失败: {e}")
            return None
