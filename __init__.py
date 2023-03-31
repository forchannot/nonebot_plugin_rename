import asyncio
import random
from pathlib import Path

from nonebot import get_driver, on_command, require, logger, get_bots
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    Message,
    GROUP_ADMIN,
    GROUP_OWNER,
    MessageSegment,
    ActionFailed,
)
from nonebot.drivers import Driver
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER

from .config.config import Config
from .utils.card_choice import choice_card, name_of_card
from .utils.my_yaml import read_yaml, write_yaml

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

scheduler = scheduler
driver: Driver = get_driver()
NICKNAME: str = list(driver.config.nickname)[0] or "Bot"
yml_file = Path.cwd() / "data" / "group_card"
env_config = Config.parse_obj(get_driver().config.dict())
hour, minute = env_config.set_group_card_hour, env_config.set_group_card_minute

group_card = on_command(
    "设置群名片",
    aliases={"更改群名片", "修改群名片"},
    permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER,
    priority=13,
    block=False,
)
view_pic = on_command(
    "查看群名片列表",
    aliases={"查看所有群名片", "群名片列表"},
    permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER,
    priority=14,
    block=False,
)
view_card = on_command(
    "查看当前群名片",
    aliases={"当前群名片"},
    permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER,
    priority=14,
    block=False,
)
set_card_now = on_command(
    "立即更改群名片",
    aliases={"立即设置群名片", "立即修改群名片"},
    permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER,
    priority=10,
    block=False,
)
del_group_card = on_command(
    "删除群名片",
    aliases={"删除本群群名片"},
    permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER,
    priority=10,
    block=False,
)


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
        int(gn) > len(name_of_card) for gn in group_nicknames
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


async def set_group_card():
    bots = get_bots()
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    if not group_data:
        return
    tasks = []
    for bot_id, bt in bots.items():
        group_info = group_data.get(bot_id, {})
        if not group_info:
            continue
        for group_id, group_nicks in group_info.items():
            card_name = await choice_card(random.choice(group_nicks))
            if card_name:
                task = bt.set_group_card(
                    group_id=group_id,
                    user_id=int(bot_id),
                    card=f"{NICKNAME}|{card_name}",
                )
                tasks.append(task)
                logger.info(f"即将为群{group_id}的bot设置群名片后缀{card_name}")
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for group_info, result in zip(group_data.values(), results):
        group_id = next(iter(group_info))
        if isinstance(result, Exception):
            logger.warning(f"群{group_id}名片更改失败，错误信息：{result}")


@view_pic.handle()
async def _(event: GroupMessageEvent):
    img = MessageSegment.image(Path(__file__).parent / "img" / "img.png")
    await view_pic.finish(message=MessageSegment.text("可以使用<更改群名片 序号>进行设置") + img)


@view_card.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    img = MessageSegment.image(Path(__file__).parent / "img" / "img.png")
    if group_data != {}:
        if str(event.group_id) in group_data[bot.self_id]:
            result = group_data[bot.self_id][str(event.group_id)]
            nicks = " ".join(result)
            result = f"当前群组设置的群名片序号有{nicks}"
        else:
            result = "当前没有设置群名片哦,请先发送<设置群名片 序号>命令进行设置吧"
    else:
        result = "当前没有设置群名片哦,请先发送<设置群名片 序号>命令进行设置吧"
    await view_card.finish(message=MessageSegment.text(result) + img)


@set_card_now.handle()
async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
    card_number = arg.extract_plain_text().strip()
    if not card_number:
        await set_card_now.finish("请输入序号或序号输入错误")
    elif card_number not in map(str, range(1, 14)):
        await set_card_now.finish("没有这种类型的群名片哦，可以发送[查看群名片列表]命令查看吧")
    else:
        card_name = await choice_card(card_number)
        card_name = f"{NICKNAME}|{card_name}"
        try:
            await bot.set_group_card(
                group_id=event.group_id, user_id=int(bot.self_id), card=card_name
            )
            logger.info(f"群组{event.group_id}成功设置名片 >> {card_name}")
        except (AttributeError, ActionFailed):
            logger.warning("更改群名片失败，可能是机器人不存在或被风控")


@del_group_card.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    if bot.self_id in group_data and str(event.group_id) in group_data[bot.self_id]:
        group_data[bot.self_id].pop(str(event.group_id))
        write_yaml(yml_file / "group_card.yaml", group_data)
        await del_group_card.finish("删除成功")
    else:
        await del_group_card.finish("本群还没设置过群名片哦")


@scheduler.scheduled_job("interval", hours=hour, minutes=minute, id="rename_group_card")
async def _():
    logger.info("开始为列表中的群更改bot群名片")
    await set_group_card()


@driver.on_startup
async def init_group_card():
    if not yml_file.exists():
        yml_file.mkdir(parents=True)
        logger.info("创建group_card文件夹成功")
    if not (yml_file / "group_card.yaml").exists():
        (yml_file / "group_card.yaml").touch()
        logger.info("创建group_card.yaml文件成功")
