# Description: 获取机器人收发消息数量

from nonebot import get_bot


async def get_msg() -> str:
    bot = get_bot()
    bot_status = await bot.get_status()
    if bot_status := bot_status.get('stat'):
        msg_received = bot_status.get('message_received', '未知')
        msg_sent = bot_status.get('message_sent', '未知')
        return f"已发送{msg_sent}条|已接收{msg_received}条"