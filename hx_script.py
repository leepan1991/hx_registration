from time_util import get_today
from mitmproxy import ctx
from mitmproxy import http
import json
import datetime
import time


def get_date_time():
    d = datetime.datetime.fromtimestamp(time.time())
    time_str = d.strftime("%Y-%m-%d %H:%M:%S:%f")
    return time_str


def request(flow):
    request = flow.request
    if request.url == 'https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Register&a=submitReg':
        cookies = dict(request.cookies)  # 转换cookies格式为dict
        urlencoded_form = dict(request.urlencoded_form)
        print(get_date_time() + "===>SubmitReg Cookies:" + str(cookies))
        print(get_date_time() + "===>SubmitReg Urlencoded_Form:" + str(urlencoded_form))
        today_timestamp_eight = get_today()
        current_time = int(time.time())
        time_diff = today_timestamp_eight + 16 - current_time
        print(get_date_time() + "===>SubmitReg diff time: " + str(time_diff))
        if time_diff > 0:
            print(get_date_time() + "===>正在等待时间到达8点，请稍后...")
            time.sleep(time_diff)
        print(get_date_time() + "===>时间到达，开始执行...")
        # ctx.master.shutdown()

    if request.url.startswith('https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Register&a=doRegQueueResult'):
        print(get_date_time() + "===>doRegQueueResult，执行...")

    if request.url.startswith('https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Register&a=realPayment'):
        print(get_date_time() + "===>realPayment，执行...")


def response(flow):
    request = flow.request
    if request.url == 'https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Register&a=checkTime':
        text = flow.response.get_text()
        print(get_date_time() + "===>CheckTime Old RESP: " + text)
        today_timestamp = get_today()
        text = text.replace(str(today_timestamp), str(today_timestamp - 45))
        print(get_date_time() + "===>CheckTime New RESP: " + text)
        flow.response.set_text(text)

    if request.url == 'https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Register&a=submitReg':
        text = flow.response.get_text()
        print(get_date_time() + "===>SubmitReg RESP: " + text)
        # resp_data = json.loads(text)
        # resp_data["state"] = 1
        # resp_data["errorMsg"] = "成功"
        # resp_data["data"] = {"type": "queue", "queueid": 100}
        # print(get_date_time() + "===>SubmitReg2 RESP: " + json.dumps(resp_data))
        # flow.response.set_text(json.dumps(resp_data))

    if request.url.startswith('https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Register&a=doRegQueueResult'):
        text = flow.response.get_text()
        print(get_date_time() + "===>DoRegQueueResult RESP: " + text)

    if request.url.startswith('https://huaxi2.mobimedical.cn/index.php?g=WapApi&m=Register&a=realPayment'):
        text = flow.response.get_text()
        print(get_date_time() + "===>RealPayment RESP: " + text)


if __name__ == '__main__':
    # time.sleep(2.35624)
    get_date_time()
