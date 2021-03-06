from selenium import webdriver
import ddt,unittest
from selenium.webdriver.common.by import By
import time,traceback
from selenium.common.exceptions import NoSuchElementException
from  DataDriverProject.log import *

@ddt.ddt
class TestDemo(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()


  list1 = (('神奇动物城','叶子'),('疯狂动物城','古德温'))
  info('测试数据{}'.format(list1))
  @ddt.data(*list1)
  @ddt.unpack
  def test_dataDriver(self,testdata,expectdata):
    info('测试数据{},{}'.format(testdata,expectdata))
    url = 'https://www.baidu.com'
    self.driver.get(url)
    info('登录地址{}'.format(url))
    self.driver.implicitly_wait(10)
    try:
       info('输入信息{}'.format(testdata))
       self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys(testdata)
       time.sleep(3)
       info('校验数据{}'.format(expectdata))
       self.assertTrue(expectdata in self.driver.page_source)
    except AssertionError as e:
       debug('核对数据不一致{}'.format(e))
    except  NoSuchElementException as e:
       debug('元素不存在{}'.format(e))
    except Exception as e:
       debug('未知错误{}'.format(e))
    else:
        info('输入{}，验证{}，通过'.format(testdata,expectdata))


if __name__ == '__main__':

  pass