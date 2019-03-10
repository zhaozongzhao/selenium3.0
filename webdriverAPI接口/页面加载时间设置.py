from selenium import webdriver
import unittest,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SetpageloadTime(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #设置页面静态等待时间
        # self.driver.set_script_timeout(10)

    # def tearDown(self):
    #     self.driver.quit()

    def test_PageLoadTime(self):
        #设定页面加载时间
        self.driver.set_page_load_timeout(4)
        self.driver.maximize_window()
        try:
           startTime = time.time()
           self.driver.get('https://mail.126.com/')
        except TimeoutException as e:
            print('页面加载时间超过设定时间')
            #通过执行javascript来停止加载，然后继续执行后续动作
            self.driver.execute_script('window.stop()')
        end = time.time()-startTime
        print(end)
        time.sleep(5)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@frameborder="0"]'))
        # wait = WebDriverWait(self.driver,20,0.5)
        # element = wait.until(EC.visibility_of(self.driver.find_element_by_xpath('//*[@id="auto-id-1551196331750"]')))
        # print(element)
        username = self.driver.find_element_by_xpath('//*[@name="email"]')
        username.send_keys('zzz')
        pwd = self.driver.find_element(By.XPATH,'//*[@name="password"]')
        pwd.send_keys('wweww')
        pwd.send_keys(Keys.RETURN)

