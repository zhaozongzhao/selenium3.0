#encoding = utf-8
from selenium import webdriver
import unittest
from Log import *

class TestSoGouSearch(unittest.TestCase):
    def setUp(self):
        #启动浏览器
        self.driver = webdriver.Chrome()

    def testSoGouSearcg(self):
        # info('#################搜索####################')
        url = 'https://www.sogou.com/'
        self.driver.get(url)
        info('访问百度界面')
        self.driver.find_element_by_id('query').send_keys('关荣之路自动化测试')

        info('再输入框输入搜索关键字‘关荣之路关荣之路自动化测试’')
        self.driver.find_element_by_id('stb').click()
        info('单击搜索按钮')
        info('=================测试用例执行完成===============')

    def tearDown(self):
        #关闭浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()