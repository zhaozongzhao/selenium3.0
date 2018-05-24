__author__ = 'zz'
#encoding=utf-8
import logging
from common import config


class Log:
    def __init__(self,log_name,file_name):
        self.log_name=log_name
        self.file_name=file_name

    def logger(self,level,msg):
        #日志收集器
        my_log=logging.getLogger(self.log_name)
        my_log.setLevel('DEBUG')

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        fh=logging.FileHandler(config.log_dir+self.file_name,encoding="utf-8")
        fh.setFormatter(formatter)
        fh.setLevel('DEBUG')

        my_log.addHandler(fh)

        if level.upper()=='DEBUG':
            my_log.debug(msg)
        elif level.upper()=='INFO':
            my_log.info(msg)
        elif level.upper()=='WARNING':
            my_log.warning(msg)
        elif level.upper()=='ERROR':
            my_log.error(msg)
        else:
            my_log.critical(msg)

        my_log.removeHandler(fh)

    def debug(self,msg):
        self.logger('debug',msg)

    def info(self,msg):
        self.logger('info',msg)

    def warning(self,msg):
        self.logger('warning',msg)

    def error(self,msg):
        self.logger('error',msg)

    def critical(self,msg):
        self.logger('critical',msg)

if __name__=='__main__':
    logger=Log("summer_liu","ython3-0109-log.txt")
    logger.info("我终于写完成了一个日志")