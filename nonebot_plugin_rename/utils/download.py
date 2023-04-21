import aiohttp
from nonebot import logger
from pathlib import Path


async def download_file(url: str, file_path: Path) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                with file_path.open(mode='wb') as f:
                    f.write(await resp.read())
                logger.info("字体文件下载成功")
            else:
                logger.error(f'下载失败，状态码：{resp.status}')