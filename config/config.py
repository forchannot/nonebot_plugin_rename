# 插件的配置文件
from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    set_group_card_hour: int = 0
    set_group_card_minute: int = 30