import os

#获取项目的绝对路径
path = os.path.dirname(os.path.dirname(__file__))

#配置文件路径（获取对象库文件的绝对路径）
PaserPageObject_path = path + '/Conf/PageObjectRepository.ini'

#数据表格路径
Excelobject_path =  path + '/Testdata/工作簿2.xlsx'

#日志文件
logobject_path =  path +'/Conf/logger.conf'

