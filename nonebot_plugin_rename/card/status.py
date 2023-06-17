# Description: 获取机器人所在系统状态

import asyncio

import psutil


async def system_status():
    mem_percent = psutil.virtual_memory().percent
    psutil.cpu_percent()
    await asyncio.sleep(0.5)
    cpu_percent = psutil.cpu_percent()
    return f"内存:{mem_percent}%|CPU:{cpu_percent}%"
