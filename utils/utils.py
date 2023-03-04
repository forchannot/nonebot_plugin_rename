import nonebot
from typing import Optional
from nonebot.adapters.onebot.v11 import Bot


def get_bot() -> Optional[Bot]:
    try:
        return list(nonebot.get_bots().values())[0]
    except IndexError:
        return None