import datetime


def gk() -> str:
    now = datetime.datetime.now()
    current_year = now.year

    # 设置目标年份的高考日期，每年的6月7日9点到6月8日17点
    gk_start = datetime.datetime(current_year, 6, 7, 9)
    gk_end = datetime.datetime(current_year, 6, 8, 17)

    # 判断是否已经超过当年的高考日期
    if now > gk_end:
        current_year += 1
        gk_start = datetime.datetime(current_year, 6, 7, 9)
        gk_end = datetime.datetime(current_year, 6, 8, 17)

    if gk_start <= now <= gk_end:
        return f"{current_year}年高考正在进行中"
    # 计算剩余时间
    remaining_time = gk_start - now
    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"距离{current_year}年高考还有{days}天{hours}小时{minutes}分钟"
