from datetime import datetime
from typing import Dict, List

from ..config import env_config


class MhyGameVersion:
    """获取米哈游游戏版本剩余时间"""

    def __init__(
        self,
        base_time_str: str,
        version_list: List,
        name: str,
        special_versions_dict: Dict[int, int],
    ):
        """
        :param base_time_str: 基准时间，str "2021-07-21 00:00:00"
        :param version_list: 游戏版本列表，list [1.1, 1.2, 1.3, 1.4...]
        :param name: 游戏名称，str "name"
        """
        self.base_time = datetime.strptime(base_time_str, "%Y-%m-%d %H:%M:%S")
        self.version_list = version_list
        self.name = name
        self.special_versions_dict = special_versions_dict

    def get_version_time(self) -> str:
        now_time = datetime.now()
        during_time = (self.base_time - now_time).total_seconds() * 1000
        index = 0
        time_conversion_factor = 24 * 60 * 60 * 1000
        while during_time <= 0:
            if (
                self.special_versions_dict
                and self.version_list[index] in self.special_versions_dict
            ):
                during_time += (
                    self.special_versions_dict[self.version_list[index]]
                    * time_conversion_factor
                )
            else:
                during_time += 42 * time_conversion_factor
            index += 1
        version = (self.version_list[index] / 10).__round__(1)
        days = int(during_time / (24 * 3600 * 1000))
        leave1 = during_time % (24 * 3600 * 1000)
        hours = int(leave1 / (3600 * 1000))
        return f"离{self.name}{version}还有{days}天{hours}小时"


starrail = MhyGameVersion(
    "2023-11-15 11:00:00",
    env_config.rename_mhy_versions["sr"].version_list,
    "崩铁",
    env_config.rename_mhy_versions["sr"].special_versions_dict,
).get_version_time

genshin = MhyGameVersion(
    "2023-8-16 11:00:00",
    env_config.rename_mhy_versions["gi"].version_list,
    "原神",
    env_config.rename_mhy_versions["gi"].special_versions_dict,
).get_version_time
