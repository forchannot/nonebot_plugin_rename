# Description: 插件的配置文件
from typing import Dict, List, Optional

from nonebot import get_driver
from pydantic import BaseModel, Extra


class MhyVersion(BaseModel):
    version_list: List[int]
    special_versions_dict: Dict[int, int]


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
    rename_mhy_versions: Dict[str, MhyVersion] = {
        "gi": MhyVersion(
            version_list=[43, 44, 45, 46, 47, 48, 50], special_versions_dict={}
        ),
        "sr": MhyVersion(
            version_list=[16, 20, 21, 22, 23, 24, 25, 26],
            special_versions_dict={16: 41, 20: 49},
        ),
    }


env_config = Config.parse_obj(get_driver().config.dict())
