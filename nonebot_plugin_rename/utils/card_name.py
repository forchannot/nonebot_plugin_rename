# Description: 群名片序号对应的函数
from ..card import (
    gaokao_time,
    genshin_time,
    get_times,
    hot_search,
    message,
    one_word,
    status,
)

card_list = {
    "1": ("原神版本剩余时间", genshin_time.genshin_version_time),
    "2": ("北京时间(小时)", get_times.now_time),
    "3": ("当前时间(古代计时制)", get_times.old_time),
    "4": ("B站热搜", hot_search.hot),
    "5": ("微博热搜", hot_search.hot),
    "6": ("抖音热搜", hot_search.hot),
    "7": ("百度热搜", hot_search.hot),
    "8": ("知乎热搜", hot_search.hot),
    "9": ("今日头条热搜", hot_search.hot),
    "10": ("每日一言", one_word.get_one_speak),
    "11": ("距离高考剩余时间", gaokao_time.gk),
    "12": ("bot系统运行状态", status.system_status),
    "13": ("bot收发消息统计", message.get_msg),
}
