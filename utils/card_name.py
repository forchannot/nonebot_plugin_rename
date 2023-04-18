# Description: 群名片序号对应的函数

from ..card import (
    genshin_time,
    get_times,
    hot_search,
    one_word,
    gaokao_time,
    status,
    message,
)

name_of_card = {
    "1": genshin_time.genshin_version_time,
    "2": get_times.now_time,
    "3": get_times.old_time,
    "4": hot_search.hot,
    "5": hot_search.hot,
    "6": hot_search.hot,
    "7": hot_search.hot,
    "8": hot_search.hot,
    "9": hot_search.hot,
    "10": one_word.get_one_speak,
    "11": gaokao_time.gk,
    "12": status.system_status,
    "13": message.get_msg,
}
card_name_list = [
    ("1", "原神版本剩余时间"),
    ("2", "北京时间(小时)"),
    ("3", "当前时间(古代计时制)"),
    ("4", "B站热搜"),
    ("5", "微博热搜"),
    ("6", "抖音热搜"),
    ("7", "百度热搜"),
    ("8", "知乎热搜"),
    ("9", "今日头条热搜"),
    ("10", "每日一言"),
    ("11", "距离高考剩余时间"),
    ("12", "bot系统运行状态"),
    ("13", "bot收发消息统计"),
]
