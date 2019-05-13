from selenium import webdriver
import ddt,unittest
from selenium.webdriver.common.by import By
import time,traceback
from selenium.common.exceptions import NoSuchElementException
from  DataDriverProject.log import *
import HTMLTestRunner
from DataDriverProject.ExcelDataDriverProject import *

execpath = 'F:\gitstorehouse\selenium3.0\DataDriverProject\\testdata.xlsx'
pe = ParseExcel(execpath, "测试")

@ddt.ddt
class TestDemo(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome()

  def tearDown(self):
      self.driver.quit()


  @ddt.data(*pe.getDataFromeSheet())
  def test_dataDriver(self,value):
    info('测试数据{}'.format(value))
    url = 'https://www.baidu.com'
    self.driver.get(url)
    info('登录地址{}'.format(url))
    self.driver.implicitly_wait(10)
    testdata,expectdata = tuple(value)
    try:
       info('输入信息{}'.format(testdata))
       self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys(testdata)
       time.sleep(3)
       info('校验数据{}'.format(expectdata))
       self.assertTrue(expectdata in self.driver.page_source)
    except AssertionError as e:
       self.assertNotIn(expectdata,self.driver.page_source)
       debug('核对数据不一致{}'.format(e))
    except  NoSuchElementException as e:
       debug('元素不存在{}'.format(e))
    except Exception as e:
       debug('未知错误{}'.format(e))
    else:
        info('输入{}，验证{}，通过'.format(testdata,expectdata))


if __name__ == '__main__':
   suite1 = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
   suite = unittest.TestSuite(suite1)
   filename = 'F:\gitstorehouse\selenium3.0\DataDriverProject\\test.html'
   fp = open(filename,'wb')
   runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description='zzz')
   runner.run(suite)
