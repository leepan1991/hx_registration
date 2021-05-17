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
        bar_code_value = bar_code_value.replace("&wxuserid=11&state=", "")
        value_split = bar_code_value.split('deptId=')
        bar_code_value = value_split[0] + "deptId=0&LabelId=24"
        print(bar_code_value)
        img = generate_bar_code(bar_code_value)
        img_name = global_config.getRaw('account', 'img_name') + ".png"
        save_image(img, img_name)

        open_image(add_bg_for_qr(img_name))
        print("====================四次decode=======================")
        print(unquote(unquote(unquote(unquote(cookies['card_list_url'])))))


if __name__ == '__main__':
    # var_name = global_config.getRaw('account', 'img_name')
    # print(var_name)
    va_te = 'https%3A//huaxi2.mobimedical.cn/index.php%3Fg%3DWap%26m%3DWxView%26d%3DregisterAndAppoint%26a%3Dindex%26wxuserid%3D11%26state%3D%23selectCard.html%3Fschedulid%3D97308%26regSchedulidInfo%3D%257B%2522date%2522%253A%25222021-05-31%2522%252C%2522docName%2522%253A%2522%25u5415%25u658C%2522%252C%2522deptname%2522%253A%2522%25u4EA7%25u79D1%25u95E8%25u8BCA%2522%252C%2522sumfee%2522%253A%252213%2522%252C%2522districtName%2522%253A%2522%25u9526%25u6C5F%25u9662%25u533A%2522%257D%26deptId%3D1336%26LabelId%3D0'
    bar_code_value = unquote(va_te)
    bar_code_value = bar_code_value.replace("&wxuserid=11&state=", "")
    print(bar_code_value)
    va_dd = bar_code_value.split('deptId=')
    print(va_dd)
    print(va_dd[0] + "deptId=0&LabelId=24")
