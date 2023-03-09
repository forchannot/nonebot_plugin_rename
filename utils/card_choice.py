from inspect import isroutine
from ..card.genshin_time import genshin_version_time
from ..card.get_times import now_time, old_time
from ..card.hot_search import hot_search
from ..card.one_word import get_one_speak
from ..card.gaokao_time import gaokao_time


def default():
    return "没有这种类型"


def choice_card(num):
    card_name = {
        "1":  genshin_version_time,
        "2":  now_time,
        "3":  old_time,
        "4":  hot_search,
        "5":  hot_search,
        "6":  hot_search,
        "7":  hot_search,
        "8":  hot_search,
        "9":  hot_search,
        "10": get_one_speak,
        "11": gaokao_time,
    }.get(num, default)
    arg = (int(num) - 3) if 4 <= int(num) <= 9 else ()
    return await card_name(*arg) if isroutine(card_name) else card_name(*arg)
