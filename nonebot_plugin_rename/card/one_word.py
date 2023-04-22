# Description: 获取一言

from typing import Optional

import httpx
from nonebot import logger


async def get_one_speak() -> Optional[str]:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            res = await client.get("https://v1.hitokoto.cn/")
            data = res.json()["hitokoto"]
            return data[:16]
        except Exception as e:
            logger.warning(f"获取一言失败: {e}")
            return None
