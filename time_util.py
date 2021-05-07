import datetime
import time


def get_today():
    today = datetime.date.today()
    formatted_today = today.strftime('%Y-%m-%d')
    a = formatted_today + " 07:59:45"
    d = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
    t = d.timetuple()
    time_stamp = int(time.mktime(t))
    return time_stamp
