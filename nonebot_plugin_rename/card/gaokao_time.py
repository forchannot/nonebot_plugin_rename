# Description: 获取高考倒计时

from datetime import datetime


def gk() -> str:
    # 基准时间
    baseTime = (
        datetime.strptime("2023-6-7 9:00:00", "%Y-%m-%d %H:%M:%S").timestamp() * 1000
    )
    nowTime = datetime.now().timestamp() * 1000
    # 获取持续时间
    duringTime = baseTime - nowTime
    while duringTime <= 0:
        # 时间+365天
        duringTime += 365 * 24 * 60 * 60 * 1000
    # 获取天数并取整
    days = int(duringTime / (24 * 3600 * 1000))
    leave1 = duringTime % (24 * 3600 * 1000)
    # 获取小时数并取整
    hours = int(leave1 / (3600 * 1000))
    leave2 = leave1 % (3600 * 1000)
    # 获取分钟数并取整
    minutes = int(leave2 / (60 * 1000))
    return f"离高考还有{days}天{hours}小时{minutes}分钟"
