# Description: 插件的配置文件
from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    set_group_card_hour: int = 0
    set_group_card_minute: int = 30
    use_nickname_front: bool = True
    self_name: str = None
    is_one_bot_set_all_group_card: bool = False