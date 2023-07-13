from datetime import datetime


class MhyGameVersion:
    """获取米哈游游戏版本剩余时间"""

    def __init__(self, base_time_str: str, version_list: list, name: str):
        """
        :param base_time_str: 基准时间，str "2021-07-21 00:00:00"
        :param version_list: 游戏版本列表，list [1.1, 1.2, 1.3, 1.4...]
        :param name: 游戏名称，str "name"
        """
        self.base_time = datetime.strptime(base_time_str, "%Y-%m-%d %H:%M:%S")
        self.version_list = version_list
        self.name = name

    def get_version_time(self) -> str:
        now_time = datetime.now()
        during_time = (self.base_time - now_time).total_seconds() * 1000
        index = 0
        while during_time <= 0:
            during_time += 42 * 24 * 60 * 60 * 1000
            index += 1
        version = (self.version_list[index] / 10).__round__(1)
        days = int(during_time / (24 * 3600 * 1000))
        leave1 = during_time % (24 * 3600 * 1000)
        hours = int(leave1 / (3600 * 1000))
        # leave2 = leave1 % (3600 * 1000)
        # minutes = int(leave2 / (60 * 1000))
        return f"离{self.name}{version}还有{days}天{hours}小时"


starrail = MhyGameVersion(
    "2023-6-7 11:00:00",
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    "崩铁",
).get_version_time

genshin = MhyGameVersion(
    "2023-4-12 11:00:00",
    [36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    "原神",
).get_version_time
