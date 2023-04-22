from nonebot.plugin import PluginMetadata

from .main import *  # noqa

__version__ = "1.2.0"
__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_rename",
    description="用于更改qq机器人的群名片，内置多种有趣名片",
    usage="查看本仓库readme",
    extra={
        "author": "forchannot",
        "version": __version__,
    }
)
