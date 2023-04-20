# Description: 获取当前时间
import datetime


def old_time() -> str:
    now = datetime.datetime.now()
    BigHourName = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥", "子"]
    BigHourType = ["正", "初"]
    # BigMinName = ["零", "一", "二", "三", "四"]
    hour = now.hour
    # minutes = now.minute
    return f"现在是长安{BigHourName[(hour + 1) // 2]}{BigHourType[hour % 2]}"


def now_time() -> str:
    now = datetime.datetime.now()
    hour = now.hour
    # minutes = now.minute
    if hour < 10:
        hour = f"0{hour}"
    # if minutes < 10:
    #     minutes = f"0{minutes}"
    return f"现在是北京时间{hour}点"
