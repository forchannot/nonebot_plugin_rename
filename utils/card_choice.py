from inspect import iscoroutinefunction
from ..card import (
    message,
    status,
    genshin_time,
    get_times,
    hot_search,
    one_word,
    gaokao_time,
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


def default():
    return "没有这种类型"


async def choice_card(num):
    card_name_choice = name_of_card.get(num, default)
    arg = (int(num) - 3,) if 4 <= int(num) <= 9 else ()
    return (
        await card_name_choice(*arg)
        if iscoroutinefunction(card_name_choice)
        else card_name_choice(*arg)
    )
