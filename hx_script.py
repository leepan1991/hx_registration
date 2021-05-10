from time_util import get_today
from mitmproxy import ctx
import time


def request(flow):
    request = flow.request
    if request.url == 'https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Register&a=submitReg':
        cookies = dict(request.cookies)  # 转换cookies格式为dict
        urlencoded_form = dict(request.urlencoded_form)
        print("SubmitReg Cookies:" + str(cookies))
        print("SubmitReg Urlencoded_Form:" + str(urlencoded_form))
        today_timestamp_eight = get_today()
        current_time = int(time.mktime(time.time()))
        time_diff = today_timestamp_eight + 15 - current_time
        print("SubmitReg diff time: " + str(time_diff))
        if time_diff > 0:
            print("正在等待时间到达8点，请稍后...")
            time.sleep(time_diff)
        print("时间到达，开始执行...")
        # ctx.master.shutdown()


def response(flow):
    request = flow.request
    if request.url == 'https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Register&a=checkTime':
        text = flow.response.get_text()
        print("CheckTime Old RESP: " + text)
        today_timestamp = get_today()
        text = text.replace(str(today_timestamp), str(today_timestamp - 45))
        print("CheckTime New RESP: " + text)
        flow.response.set_text(text)

    if request.url == 'https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Register&a=submitReg':
        text = flow.response.get_text()
        print("SubmitReg RESP: " + text)


if __name__ == '__main__':
    time.sleep(2.35624)
