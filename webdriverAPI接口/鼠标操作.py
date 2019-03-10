from selenium import webdriver
import unittest
from time import sleep

class Mose(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.close()

    #鼠标点击左键和释放左键
    def test_simulationLeftClickMoseOfProcess(self):
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\鼠标左键按下与释放.html'
        #访问自定义的Html网页
        self.driver.get(url)
        div =  self.driver.find_element_by_id('div1')
        from selenium.webdriver import ActionChains
        import time

        ActionChains(self.driver).click_and_hold(div).perform()
        time.sleep(2)
        ActionChains(self.driver).release(div).perform()
        ActionChains(self.driver).click_and_hold(div).perform()
        ActionChains(self.driver).release(div).perform()
        time.sleep(10)

     #鼠标悬停操作
    def test_roverOnElement(self):
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\鼠标悬停.html'
        self.driver.get(url)
        #定位链接的元素
        link1 =  self.driver.find_element_by_partial_link_text('指过来1')
        link2 = self.driver.find_element_by_partial_link_text('指过来2')
        #定位p元素
        p =  self.driver.find_element_by_xpath('/html/body/p')
        print(link1.text,link2.text)
        from selenium.webdriver import ActionChains
        import time
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(link1).perform()
        time.sleep(2)
        action_chains.move_to_element(p).perform()
        time.sleep(2)
        action_chains.move_to_element(link2).perform()
        time.sleep(2)
        action_chains.move_to_element(p).perform()
        time.sleep(2)

    #判断元素是否存在

    def test_isElementPresent(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        res = self.isElementPresent('id','query')
        if res is True:
            print('元素存在')
        else:
            print('元素不存在')

    def isElementPresent(self,by,value):
        from selenium.common.exceptions import NoSuchElementException
        try:
            element = self.driver.find_element(by=by,value=value)
        except NoSuchElementException as a:

            print(a)
            return False
        else:
            return True

