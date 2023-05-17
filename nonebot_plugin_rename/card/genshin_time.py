# Description: 获取原神版本剩余时间
from datetime import datetime


def genshin_version_time() -> str:
    # 原神版本号
    Versions = [36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    Index = 0
    # 获取持续时间
    baseTime = datetime.strptime('2023-4-12 11:00:00', '%Y-%m-%d %H:%M:%S')
    nowTime = datetime.now()
    duringTime = (baseTime - nowTime).total_seconds() * 1000
    # 推算版本
    while duringTime <= 0:
        duringTime += 42 * 24 * 60 * 60 * 1000
        Index += 1
    # 计算版本号并取到小数点后一位
    Version = (Versions[Index] / 10).__round__(1)
    # 获取天数并取整
    days = int(duringTime / (24 * 3600 * 1000))
    leave1 = duringTime % (24 * 3600 * 1000)
    # 获取小时数并取整
    hours = int(leave1 / (3600 * 1000))
    leave2 = leave1 % (3600 * 1000)
    # 获取分钟数并取整
    minutes = int(leave2 / (60 * 1000))
    # 字符串处理
    return f'离原神{Version}还有{days}天{hours}小时{minutes}分钟'
