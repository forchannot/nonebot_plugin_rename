# Description: 获取星穹铁道版本剩余时间
from datetime import datetime


def starrail_version_time() -> str:
    # 基准版本
    Version = 1.1
    baseTime = (
        datetime.strptime("2023-6-7 11:00:00", "%Y-%m-%d %H:%M:%S").timestamp() * 1000
    )
    nowTime = datetime.now().timestamp() * 1000
    # 获取持续时间
    duringTime = baseTime - nowTime
    while duringTime <= 0:
        # 版本+0.1 同时时间+42天
        duringTime += 42 * 24 * 60 * 60 * 1000
        Version += 0.1
    # 获取天数并取整
    days = int(duringTime / (24 * 3600 * 1000))
    leave1 = duringTime % (24 * 3600 * 1000)
    # 获取小时数并取整
    hours = int(leave1 / (3600 * 1000))
    leave2 = leave1 % (3600 * 1000)
    # 获取分钟数并取整
    minutes = int(leave2 / (60 * 1000))
    return f"离崩铁{Version:.1f}还有{days}天{hours}小时{minutes}分钟"

