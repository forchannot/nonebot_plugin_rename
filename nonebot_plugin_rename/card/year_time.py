import datetime


def next_year_time() -> str:
    # 获取当前日期和时间
    now = datetime.datetime.now()

    # 指定目标年份
    target_year = now.year + 1  # 下一年

    # 构造目标日期
    target_date = datetime.datetime(target_year, 1, 1)

    # 计算时间差
    time_difference = target_date - now

    # 计算剩余天、小时、分钟和秒
    total_seconds = time_difference.total_seconds()
    days = int(total_seconds // (24 * 3600))
    hours = int((total_seconds % (24 * 3600)) // 3600)
    minutes = int((total_seconds % 3600) // 60)

    # 输出结果
    return f"距离{target_year}年还有{days}天{hours}小时{minutes}分"
