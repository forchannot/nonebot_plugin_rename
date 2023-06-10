from datetime import datetime

from ..config import env_config


class ExamTime:
    def __init__(self, exam: str, base_time: tuple):
        """
        :param exam: 考试名称
        :param base_time: 考试时间，格式为("2021-06-07 09:00:00", "2021-06-08 17:00:00")
        """
        self.exam = exam
        self.base_time_start = datetime.strptime(base_time[0], "%m-%d %H:%M:%S")
        self.base_time_end = datetime.strptime(base_time[1], "%m-%d %H:%M:%S")

    def get_exam_time(self) -> str:
        now = datetime.now()
        current_year = now.year
        exam_start = self.base_time_start.replace(year=current_year)
        exam_end = self.base_time_end.replace(year=current_year)

        # 判断是否已经超过当年的高考日期
        if now > exam_end:
            current_year += 1
            exam_start = exam_start.replace(year=current_year)
            exam_end = exam_end.replace(year=current_year)

        if exam_start <= now <= exam_end:
            return f"{current_year}年{self.exam}正在进行中"
        # 计算剩余时间
        remaining_time = exam_start - now
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"距离{current_year}年{self.exam}还有{days}天{hours}小时{minutes}分钟"


zk = ExamTime("中考", (env_config.zk_time_start, env_config.zk_time_end)).get_exam_time
gk = ExamTime("高考", ("06-07 09:00:00", "06-08 17:00:00")).get_exam_time
ky = ExamTime("考研", ("12-23 08:30:00", "12-24 17:00:00")).get_exam_time  # 24考研
