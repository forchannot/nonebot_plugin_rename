from nonebot.plugin import PluginMetadata

from .main import *  # noqa
from .config import env_config

__version__ = "1.3.8"
__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_rename",
    description="用于更改qq机器人的群名片，内置多种有趣名片",
    usage="查看本仓库readme",
    supported_adapters={"~onebot.v11"},
    type="application",
    config=env_config,
    homepage="https://github.com/forchannot/nonebot_plugin_rename",
    extra={
        "author": "forchannot",
        "version": __version__,
    }
)
