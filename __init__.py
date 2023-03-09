import random
from pathlib import Path

from nonebot import get_driver, on_command, require, logger
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
from .utils.card_choice import choice_card
from .utils.my_yaml import read_yaml, write_yaml
from .utils.utils import get_bot

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

scheduler = scheduler
driver: Driver = get_driver()
NICKNAME: str = list(driver.config.nickname)[0]
yml_file = Path.cwd() / "data" / "group_card"
env_config = Config.parse_obj(get_driver().config.dict())
hour = env_config.set_group_card_hour
minute = env_config.set_group_card_minute

group_card = on_command(
    "设置群名片",
    aliases={"更改群名片", "修改群名片"},
    permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER,
    priority=13,
    block=False,
)
view_pic = on_command(
    "查看群名片列表",
    aliases={"查看所有群名片"},
    permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER,
    priority=14,
    block=False,
)
view_card = on_command(
    "查看当前群名片",
    permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER,
    priority=14,
    block=False,
)
set_card_now = on_command(
    "立即更改群名片",
    permission=SUPERUSER | GROUP_ADMIN | GROUP_OWNER,
    priority=10,
    block=False,
)


@group_card.handle()
async def get_group_card(bot: Bot, event: GroupMessageEvent):
    group_nicknames = str(event.get_message()).strip().split()[1:]
    group_id = str(event.group_id)
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    if group_nicknames:
        if not any(int(gn) > 13 for gn in group_nicknames):
            if group_id in group_data:
                group_data.pop(group_id)
            group_data[group_id] = group_nicknames
            write_yaml(yml_file / "group_card.yaml", group_data)
            await group_card.finish(f"已为你更改该群群名片序号为{group_nicknames}")
        else:
            await group_card.finish("没有这种群名片哦")
    else:
        if group_id in group_data:
            group_data.pop(group_id)
            write_yaml(yml_file / "group_card.yaml", group_data)
            await group_card.finish("已为你删除该群群名片设置")
        else:
            await group_card.finish("请输入你想要设置的群名片序号")


async def set_group_card():
    bot = get_bot()
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    if group_data != {}:
        for g in group_data:
            card_number = random.choice(group_data[g])
            card_name = await choice_card(card_number)
            card_name = f"{NICKNAME}|{card_name}"
            try:
                await bot.set_group_card(
                    group_id=g, user_id=int(bot.self_id), card=card_name
                )
            except AttributeError:
                logger.warning("更改群名片", "失败,可能是机器人不存在")
            except ActionFailed:
                logger.warning("更改群名片", "失败,可能是机器人不存在被风控")


@view_pic.handle()
async def _(event: GroupMessageEvent):
    img = MessageSegment.image(Path(__file__).parent / "img" / "img.png")
    await view_pic.finish(message=MessageSegment.text("可以使用<更改群名片 序号>进行更改") + img)


@view_card.handle()
async def _(event: GroupMessageEvent):
    group_data = read_yaml(yml_file / "group_card.yaml") or {}
    img = MessageSegment.image(Path(__file__).parent / "img" / "img.png")
    if group_data != {}:
        if str(event.group_id) in group_data:
            result = group_data[str(event.group_id)]
            result = f"当前群组设置的群名片序号有{result}"
        else:
            result = "当前没有设置群名片哦,请先发送<设置群名片 序号>命令进行设置吧"
    else:
        result = "当前没有设置群名片哦,请先发送<设置群名片 序号>命令进行设置吧"
    await view_card.finish(message=MessageSegment.text(result) + img)


@set_card_now.handle()
async def _(bot: Bot, event: GroupMessageEvent, arg: Message = CommandArg()):
    card_number = arg.extract_plain_text().strip()
    if card_number in list(map(str, range(1, 14))):
        card_name = await choice_card(card_number)
        card_name = f"{NICKNAME}|{card_name}"
        await bot.set_group_card(
            group_id=event.group_id, user_id=int(bot.self_id), card=card_name
        )
        logger.info(f"群组{event.group_id}成功设置名片 >> {card_name}")
    else:
        await set_card_now.finish("没有这种类型的群名片哦,可以发送[查看群名片列表]命令查看吧")


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
