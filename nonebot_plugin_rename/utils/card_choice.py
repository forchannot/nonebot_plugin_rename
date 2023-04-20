# Description: 根据卡片数字获取卡片名称
from inspect import iscoroutinefunction
from .card_name import card_list


async def choice_card(num) -> str:
    card_name_choice = card_list.get(num, "ee")[1]
    if card_name_choice == "e":
        return "没有这种类型"
    arg = (int(num) - 3,) if 4 <= int(num) <= 9 else ()
    return (
        await card_name_choice(*arg)
        if iscoroutinefunction(card_name_choice)
        else card_name_choice(*arg)
    )
