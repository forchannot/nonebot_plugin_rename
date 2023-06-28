# Description: 插件的配置文件
from typing import Optional

from nonebot import get_driver
from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    set_group_card_hour: int = 0
    set_group_card_minute: int = 30
    use_nickname_front: bool = True
    is_show_hot_search_from: bool = False
    self_name: Optional[str] = None
    is_one_bot_set_all_group_card: bool = False
    is_show_aps_info_log: bool = True
    zk_time_start: str = "06-12 09:00:00"
    zk_time_end: str = "06-14 11:00:00"
    hot_search_url: int = 1


env_config = Config.parse_obj(get_driver().config.dict())
