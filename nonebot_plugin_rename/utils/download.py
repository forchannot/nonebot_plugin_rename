from pathlib import Path

import aiofiles
import aiohttp
import tqdm
from nonebot import logger


async def download_file(url: str, file_path: Path) -> None:
    logger.info("开始下载字体文件")
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                file_size = int(resp.headers.get("content-length", 0))
                if resp.status == 200:
                    async with aiofiles.open(file_path, "wb") as f:
                        pbar = tqdm.tqdm(
                            total=file_size, unit="B", unit_scale=True
                        )
                        async for chunk in resp.content.iter_chunked(1024):
                            await f.write(chunk)
                            pbar.update(len(chunk))
                    pbar.close()
                    logger.info("字体文件下载成功")
                else:
                    logger.error(f"下载失败，状态码：{resp.status}")
        except Exception as e:
            logger.error(f"下载失败，错误信息：{e}")
