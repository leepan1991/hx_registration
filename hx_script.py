from mitmproxy import ctx
from urllib.parse import unquote
from image_util import save_image, generate_bar_code, open_image, add_bg_for_qr, image_add_text
from config import global_config


def request(flow):
    request = flow.request
    if request.url == 'https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Card&a=cardList':
        cookies = dict(request.cookies)  # 转换cookies格式为dict
        print(str(cookies))
        print("==================原始=========================")
        print(cookies['card_list_url'])
        print("====================一次decode=======================")
        bar_code_value = unquote(cookies['card_list_url'])
        print(bar_code_value)
        img = generate_bar_code(bar_code_value)
        img_name = global_config.getRaw('account', 'img_name') + ".png"
        save_image(img, img_name)

        open_image(add_bg_for_qr(img_name))
        print("====================四次decode=======================")
        print(unquote(unquote(unquote(unquote(cookies['card_list_url'])))))


if __name__ == '__main__':
    # add_bg_for_qr('test.png')
    # img = image_add_text("test.png", '李攀_592328410', 50, 100, text_color=(0, 0, 0), text_size=20)
    # save_image(img, 'test.png')
    var_name = global_config.getRaw('account', 'img_name')
    print(var_name)
