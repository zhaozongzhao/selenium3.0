import logging
import logging.config
from PageJectVar.var import *

#读取配置文件
logging.config.fileConfig(logobject_path)

#选择日志格式
logger =  logging.getLogger('example02')


def error(message):
    logging.error(message)

def info(message):
    logging.info(message)

def debug(message):
    logging.debug(message)

if __name__ == '__main__':

 info('测试')
 error('测试1')
 debug('测试2')