import logging
import logging.config

logobject_path =  'F:\gitstorehouse\selenium3.0\DataDriverProject'

#读取配置文件
# logging.config.fileConfig('F:/gitstorehouse/selenium3.0/data_driven/Conf/logger.conf')
logging.config.fileConfig(logobject_path, defaults=None, disable_existing_loggers=True)

#选择日志格式
logger =  logging.getLogger('example02')


def error(message):
    logging.error(message)

def info(message):
    logging.info(message)

def debug(message):
    logging.debug(message)

if __name__ == '__main__':

 info('再输入框输入搜索关键字‘关荣之路关荣之路自动化测试’')