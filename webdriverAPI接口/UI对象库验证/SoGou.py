from selenium import webdriver
import unittest
import time,traceback
from UI对象库验证.ObjectMap import objectmap
class TestSoGouByObjectMap(unittest.TestCase):
    def setUp(self):
        self.obj = objectmap()
        self.driver = webdriver.Chrome()

    def test1(self):
        url = 'https://www.sogou.com'
        self.driver.get(url)
        # try:
        searchbox = self.obj.getElementObjext(self.driver,'sogou','search')
        searbutton = self.obj.getElementObjext(self.driver,'sogou','searchbutton')
        searchbox.send_keys('selenium')
        searbutton.click()
        time.sleep(2)
        self.assertTrue('selenium' in self.driver.page_source)


        # except Exception as a:
        #     raise a
