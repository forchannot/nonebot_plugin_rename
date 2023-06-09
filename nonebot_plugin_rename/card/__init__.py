from .gaokao_time import gk
from .genshin_time import genshin_version_time
from .get_times import now_time, old_time
from .hot_search import hot
from .message import get_msg
from .one_word import get_one_speak
from .starrail_time import starrail_version_time
from .status import system_status
from .year_time import next_year_time

__all__ = [
    "gk",
    "genshin_version_time",
    "starrail_version_time",
    "now_time",
    "old_time",
    "hot",
    "get_msg",
    "get_one_speak",
    "system_status",
    "next_year_time",
]
