# Description: 获取机器人所在系统状态

import asyncio
import psutil


async def system_status():
    mem = psutil.virtual_memory()
    # 系统总计内存
    zj = float(mem.total) / 1024 / 1024 / 1024
    # 系统已经使用内存
    ysy = float(mem.used) / 1024 / 1024 / 1024
    # 系统空闲内存
    # kx = round(float(mem.free) / 1024 / 1024 / 1024, 1)
    # 系统已使用内存百分比
    mem_percent = round(ysy / zj * 100, 1)
    psutil.cpu_percent()
    await asyncio.sleep(0.1)
    cpu_percent = psutil.cpu_percent()
    return f"内存:{mem_percent}%|CPU:{cpu_percent}%"
