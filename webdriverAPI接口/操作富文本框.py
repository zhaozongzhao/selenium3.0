
from selenium import webdriver
import unittest,time,traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.by import By

class TestDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_SoHuMailSendEMail(self):
        url ='https://mail.sohu.com'
        self.driver.get(url)
        self.driver.maximize_window()

        try:
            uasename = self.driver.find_element(By.XPATH,'//*[@id="theme"]/form/div[1]/div[1]/input')
            uasename.clear()
            uasename.send_keys('zongzhao4117@sohu.com')
            password = self.driver.find_element(By.XPATH,'//*[@id="theme"]/form/div[2]/div[1]/input')
            password.send_keys('zzz284117')
            loginbutton = self.driver.find_element(By.XPATH,'//*[@id="theme"]/form/div[5]/input')
            loginbutton.click()
            wait = WebDriverWait(self.driver,10,0.5)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//li[text()= "写邮件"]')))
            self.driver.find_element(By.XPATH,'//li[text()= "写邮件"]').click()
            time.sleep(2)
            receiver = self.driver.find_element(By.XPATH,'//div[@arr="mail.to_render"]//input')
            receiver.send_keys('2206321864@qq.com')
            time.sleep(3)
            suobject = self.driver.find_element(By.XPATH,'//input[@ng-model="mail.subject"]')
            suobject.click()
            suobject.send_keys('正文验证')
            time.sleep(1)
            #通过switch_to 切换为frame
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//*[@id="ueditor_0"]'))
            editBox = self.driver.find_element(By.XPATH,'/html/body')
            editBox.send_keys('邮件正文')
            #跳出frame
            self.driver.switch_to.default_content()
            self.driver.find_element(By.XPATH,'//span[.="发送"]').click()
            wait.until(EC.visibility_of_element_located((By.XPATH,'//span[text = "发送成功"]')))
        except Exception:
            print(traceback.print_exc())

    def test_sohumail(self):
        url = 'https://mail.sohu.com'
        self.driver.get(url)
        self.driver.maximize_window()
        uasename = self.driver.find_element(By.XPATH, '//*[@id="theme"]/form/div[1]/div[1]/input')
        uasename.clear()
        uasename.send_keys('zongzhao4117@sohu.com')
        password = self.driver.find_element(By.XPATH, '//*[@id="theme"]/form/div[2]/div[1]/input')
        password.send_keys('zzz284117')
        loginbutton = self.driver.find_element(By.XPATH, '//*[@id="theme"]/form/div[5]/input')
        loginbutton.click()
        wait = WebDriverWait(self.driver, 10, 0.5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//li[text()= "写邮件"]')))
        self.driver.find_element(By.XPATH, '//li[text()= "写邮件"]').click()
        time.sleep(2)
        receiver = self.driver.find_element(By.XPATH, '//div[@arr="mail.to_render"]//input')
        receiver.send_keys('2206321864@qq.com')
        time.sleep(3)
        suobject = self.driver.find_element(By.XPATH, '//input[@ng-model="mail.subject"]')
        suobject.click()
        suobject.send_keys('正文验证')
        time.sleep(1)
        #通过switch_to
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//*[@id="ueditor_0"]'))
        time.sleep(2)
        #通过javascript将页面内容输入到富文本框中
        self.driver.execute_script("document.getElementsByTagName('body')[0].innerHTML='<b>测试数据<b>;'")
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, '//span[.="发送"]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text = "发送成功"]')))



