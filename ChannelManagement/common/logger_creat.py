import time
from common import logger


def loggingcreate():
     filename=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+ '.log'
     logger1=logger.Log("zzz",filename )
     return logger1
