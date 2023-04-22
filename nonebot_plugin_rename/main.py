import asyncio
import random
from pathlib import Path
from typing import List

from nonebot import get_driver, on_command, require, logger, get_bots
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    Message,
    GROUP_ADMIN,
    GROUP_OWNER,
    MessageSegment,
    ActionFailed, PrivateMessageEvent,
)
from nonebot.drivers import Driver
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER

from .config import Config
from .utils import (
    choice_card,
    generate_card_image,
    card_list,
    read_yaml,
    write_yaml,
    download_file,
)

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

driver: Driver = get_driver()
env_config = Config.parse_obj(get_driver().config.dict())
hour, minute = env_config.set_group_card_hour, env_config.set_group_card_minute
if driver.config.nickname:
    NICKNAME = (
        env_config.self_name
        if env_config.self_name
        else list(driver.config.nickname)[0]
    )
else:
    NICKNAME = env_config.self_name if env_config.self_name else "bot"
yml_file = Path.cwd() / "data" / "group_card"
permissions = SUPERUSER | GROUP_ADMIN | GROUP_OWNER

group_card = on_command(
    "设置群名片",
    aliases={"更改群名片", "修改群名片"},
    permission=permissions,
    priority=13,
    block=True,
)
view_pic = on_command(
    "查看群名片列表",
    aliases={"查看所有群名片", "群名片列表"},
    permission=permissions,
    priority=14,
    block=True,
)
view_card = on_command(
    "查看当前群名片",
    aliases={"当前群名片"},
    permission=permissions,
    priority=14,
    block=True,
)
set_card_now = on_command(
    "立即更改群名片",
    aliases={"立即设置群名片", "立即修改群名片"},
    permission=permissions,
    priority=10,
    block=True,
)
del_group_card = on_command(
    "删除群名片",
    aliases={"删除本群群名片"},
    permission=permissions,
    priority=10,
    block=True,
)
set_all_group_card = on_command(
    "更改所有群名片",
    aliases={"设置所有群名片", "修改所有群名片"},
    permission=SUPERUSER,
    priority=10,
    block=True,
)


# on_command "设置群名片"
@group_card.handle()
async def get_group_card(bot: Bot, event: GroupMessageEvent):
    # 解析参数
    group_nicknames = str(event.get_message()).strip().split()[1:]
    nicks = " ".join(group_nicknames)
    if not group_nicknames:
        await group_card.finish("请输入你想要设置的群名片序号")
    group_id = str(event.group_id)
    bot_id = bot.self_id
    # 读取群名片数据
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    group_nicknames_valid = not any(
        int(gn) > len(card_list) for gn in group_nicknames
    )  # 判断用户输入的群名片序号是否有效
    # 更新群名片数据
    if group_nicknames_valid:
        group_data.setdefault(bot_id, {})
        group_data[bot_id].setdefault(group_id, {})
        group_data[bot_id][group_id] = group_nicknames
        write_yaml(yml_file / "group_card.yaml", group_data)
        await group_card.finish(f"已为你更改该群群名片序号为{nicks}")
    else:
        await group_card.finish("没有这种群名片哦")


# 定时任务执行函数
async def set_group_card(is_handle: bool = False):
    tasks = []
    set_wrong = []
    bots = get_bots()
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    if not group_data:
        return
    for bot_id, bot_case in bots.items():
        group_info = group_data.get(bot_id, {})
        if not group_info:
            continue
        tasks.extend(await set_card(group_info, bot_id, bot_case))
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for group_info, result in zip(group_data.values(), results):
        group_id = next(iter(group_info))
        if isinstance(result, Exception):
            logger.warning(f"群{group_id}名片更改失败，错误信息：{result}")
            set_wrong.append(group_id)
    if is_handle:
        return set_wrong


# on_command "查看群名片列表"
@view_pic.handle()
async def _(event: GroupMessageEvent):
    img = MessageSegment.image(generate_card_image())
    await view_pic.finish(message=MessageSegment.text("可以使用<更改群名片 序号>进行设置") + img)


# on_command "查看当前群名片"
@view_card.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    img = MessageSegment.image(generate_card_image())
    if str(event.group_id) in group_data.get(bot.self_id, {}):
        result = group_data[bot.self_id][str(event.group_id)]
        nicks = " ".join(result)
        result = f"当前群组设置的群名片序号有{nicks}"
    else:
        result = "当前没有设置群名片哦,请先发送<设置群名片 序号>命令进行设置吧"
    await view_card.finish(message=MessageSegment.text(result) + img)


# on_command "立即更改群名片"
@set_card_now.handle()
async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
    card_number = arg.extract_plain_text().strip()
    if not card_number:
        await set_card_now.finish("请输入序号或序号输入错误")
    elif card_number not in map(str, range(1, 14)):
        await set_card_now.finish("没有这种类型的群名片哦，可以发送[查看群名片列表]命令查看吧")
    card_names = await choice_card(card_number)
    if env_config.use_nickname_front:
        card_names = f"{NICKNAME}|{card_names}"
    try:
        await bot.set_group_card(
            group_id=event.group_id, user_id=int(bot.self_id), card=card_names
        )
        logger.info(f"群组{event.group_id}成功设置名片 >> {card_names}")
    except (AttributeError, ActionFailed):
        logger.warning("更改群名片失败，可能是机器人不存在或被风控")


# on_command "删除群名片"
@del_group_card.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    if bot.self_id in group_data and str(event.group_id) in group_data[bot.self_id]:
        group_data[bot.self_id].pop(str(event.group_id))
        write_yaml(yml_file / "group_card.yaml", group_data)
        await del_group_card.finish("删除成功")
    else:
        await del_group_card.finish("本群还没设置过群名片哦")


# on_command "设置所有群名片"
@set_all_group_card.handle()
async def _(bot: Bot, event: PrivateMessageEvent):
    if env_config.is_one_bot_set_all_group_card:
        result = await set_group_card(is_handle=True)
        msg = f"群名片设置成功,设置失败的群有\n{' '.join(result)}" if result else "所有群名片设置成功"
        await set_all_group_card.finish(msg)
    set_wrong = []
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    group_info = group_data.get(bot.self_id, {})
    if not group_info:
        await set_all_group_card.finish("没有设置过任何群名片哦")
    tasks = await set_card(group_info, bot.self_id, bot)
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for group_info, result in zip(group_data.values(), results):
        group_id = next(iter(group_info))
        if isinstance(result, Exception):
            logger.warning(f"群{group_id}名片更改失败，错误信息：{result}")
            set_wrong.append(group_id)
    msg = f"群名片设置成功,设置失败的群有\n{' '.join(set_wrong)}" if set_wrong else "所有群名片设置成功"
    await set_all_group_card.finish(msg)


async def set_card(group_info: dict, bot_id: str, bot_case) -> List:
    tasks = []
    for group_id, group_nicks in group_info.items():
        card_names = await choice_card(random.choice(group_nicks))
        if env_config.use_nickname_front:
            card_names = f"{NICKNAME}|{card_names}"
        if card_names:
            tasks.append(
                bot_case.set_group_card(
                    group_id=group_id,
                    user_id=int(bot_id),
                    card=card_names,
                )
            )
            logger.info(f"即将为群{group_id}的bot设置群名片后缀{card_names}")
    return tasks


# 定时任务入口
@scheduler.scheduled_job("interval", hours=hour, minutes=minute, id="rename_group_card")
async def _():
    logger.info("开始为列表中的群更改bot群名片")
    await set_group_card()


# bot启动时执行
@driver.on_startup
async def init_group_card():
    if not (yml_file / "group_card.yaml").exists():
        yml_file.mkdir(parents=True, exist_ok=True)
        (yml_file / "group_card.yaml").touch()
        logger.info("创建group_card.yaml文件成功")
    if not (yml_file / "fonts" / "draw.ttf").exists():
        (yml_file / "fonts").mkdir(parents=True, exist_ok=True)
        await download_file(
            url="https://fastly.jsdelivr.net/gh/forchannot/nonebot_plugin_rename@main/data/fonts/draw.ttf",
            file_path=yml_file / "fonts" / "draw.ttf",
        )
