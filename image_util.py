import os
import qrcode
from PIL import ImageFont, ImageDraw, Image


def generate_bar_code(bar_value):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(bar_value)
    qr.make(fit=True)

    img = qr.make_image(fill_color="green", back_color="white")
    return img

def image_add_text(img_path, text, left, top, text_color=(255, 0, 0), text_size=20):
    img = Image.open(img_path)
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式 这里的SimHei.ttf需要有这个字体
    fontStyle = ImageFont.truetype("SimHei.ttf", text_size, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, text_color, font=fontStyle)
    return img


def open_image(image_file):
    if os.name == "nt":
        os.system('start ' + image_file)  # for Windows
    else:
        if os.uname()[0] == "Linux":
            if "deepin" in os.uname()[2]:
                os.system("deepin-image-viewer " + image_file)  # for deepin
            else:
                os.system("eog " + image_file)  # for Linux
        else:
            os.system("open " + image_file)  # for Mac


def save_image(img, image_file):
    with open(image_file, 'wb') as f:
        img.save(f)
        # image_add_text(image_file, 'testtest', 50, 100, text_color=(0, 0, 0), text_size=20)


def add_bg_for_qr(qr_path):
    try:
        from PIL import Image
        qr = Image.open(qr_path)
        w = qr.width
        h = qr.width
        bg = Image.new("RGBA", (w * 2, h * 2), (255, 255, 255))
        result = Image.new(bg.mode, (w * 2, h * 2))
        result.paste(bg, box=(0, 0))
        result.paste(qr, box=(int(w / 2), int(h / 2)))
        result.save(qr_path)
        return os.path.abspath(qr_path)
    except ImportError:
        print("加载PIL失败，不对登录二维码进行优化，请查看requirements.txt")
        return qr_path
