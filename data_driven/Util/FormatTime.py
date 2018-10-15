import time
from datetime import timedelta,date

def date_time_chinese():
    return time.strftime('%Y年%m月%d日 %H时%M分%S秒',time.localtime())

def date_chinese():
    return time.strftime('%Y年%m月%d日',time.localtime())

def date_chinese():
    return time.strftime('%H时%M分%S秒',time.localtime())

def date_time():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

def date_time_slash():
    return time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())

def dates():
    return time.strftime('%Y-%m-%d',time.localtime())

def date_slash():
    return time.strftime('%Y/%m/%d',time.localtime())

def times():
    return time.strftime('%H:%M:%S',time.localtime())

def year():
    return time.strftime('%Y',time.localtime())

def month():
    return time.strftime('%m',time.localtime())

def day():
    return time.strftime('%d',time.localtime())

def Hour():
    return time.strftime('%H',time.localtime())

def minute():
    return  time.strftime('%M',time.localtime())

def second():
    return  time.strftime('%S',time.localtime())

if __name__ == '__main__':
    print(date_time_chinese())
    print(date_chinese())
    print(date_chinese())
    print(date_time())
    print(date_time_slash())
    print(date_slash())
    print(times())
    print(year())
    print(month())
    print(day())
    print(Hour())
    print(minute())
    print(second())