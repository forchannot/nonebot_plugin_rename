# Description: 群名片序号对应的函数
from ..card import (
    genshin_version_time,
    get_msg,
    get_one_speak,
    gk,
    hot,
    now_time,
    old_time,
    system_status,
)

card_list = {
    "1": ("原神版本剩余时间", genshin_version_time),
    "2": ("北京时间(小时)", now_time),
    "3": ("当前时间(古代计时制)", old_time),
    "4": ("B站热搜", hot),
    "5": ("微博热搜", hot),
    "6": ("抖音热搜", hot),
    "7": ("百度热搜", hot),
    "8": ("知乎热搜", hot),
    "9": ("今日头条热搜", hot),
    "10": ("每日一言", get_one_speak),
    "11": ("距离高考剩余时间", gk),
    "12": ("bot系统运行状态", system_status),
    "13": ("bot收发消息统计", get_msg),
}
