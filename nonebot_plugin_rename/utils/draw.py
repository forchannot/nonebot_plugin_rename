from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

from .card_name import card_list


font_path = Path.cwd() / "data" / "group_card" / "fonts" / "draw.ttf"


def generate_card_image(
    font: Path = font_path,
    font_size: int = 20,
    title_left: str = "群名片序号",
    title_right: str = "群名片描述",
):
    # 创建一个空白的图片
    img = Image.new("RGB", (800, len(card_list) * 50 + 50), color="white")
    # 设置字体和字号
    font = ImageFont.truetype(font.as_posix(), size=font_size)
    # 创建一个绘制对象
    draw = ImageDraw.Draw(img)
    # 绘制标题和分割线
    draw.text((50, 10), title_left, font=font, fill="black")
    draw.line((200, 0, 200, len(card_list) * 50 + 50), fill="black")
    draw.text((220, 10), title_right, font=font, fill="black")
    draw.line((0, 50, 800, 50), fill="black")
    # 遍历列表，获取内容并绘制到图片上
    for i in range(len(card_list)):
        if card_list[str(i + 1)][0]:
            draw.text((95, i * 50 + 65), str(i + 1), font=font, fill="black")
            draw.line((200, i * 50 + 50, 200, (i + 1) * 50 + 50), fill="black")
            draw.text(
                (220, i * 50 + 65), card_list[str(i + 1)][0], font=font, fill="black"
            )
            draw.line((0, (i + 1) * 50 + 50, 800, (i + 1) * 50 + 50), fill="black")
    # 返回base64编码后的图片字符串
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    return img_buffer.getvalue()
