import unittest
from selenium import webdriver
import time

def hightlightElement(driver,element):
    #封装好高亮显示元素
    driver.execute_script('arguments[0].setAttribute("style",arguments[1]);',
                          element,'background:green; border:2px solid red;')
class TestDemo(unittest.TestCase):

        def setUp(self):
            self.driver = webdriver.Chrome()

        def tearDown(self):
            self.driver.quit()

        def test_HightLoghtWebelement(self):
            url = 'https://www.baidu.com/'
            self.driver.get(url)
            searchinput = self.driver.find_element_by_xpath('//*[@id="kw"]')
            hightlightElement(self.driver,searchinput)
            time.sleep(3)
            searchinput.send_keys('测试设备')
            time.sleep(3)
            button = self.driver.find_element_by_xpath('//*[@id="su"]')
            hightlightElement(self.driver,button)
            button.click()
            time.sleep(3)
            assert  '测试' in self.driver.page_source