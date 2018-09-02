from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import traceback
from data_driven.Util.ParsePageObjectRepository import *
from data_driven.PageJectVar.var import *

class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.paser_page_object = ParsePageObjectRepository()
        self.login_iteim = self.paser_page_object.getItemSection('qqmail_login')
        print(self.login_iteim)
        self.wait = WebDriverWait(self.driver,10,0.2)

    def getFrame(self):
        locateType,locateExpression  =  self.login_iteim['login_page.frame'].split('>')
        print(locateType,locateExpression)
        frame = self.wait.until(lambda x : x.find_element(by=locateType,value = locateExpression))
        return frame
    def getclick(self):
        locateType, locateExpression = self.login_iteim['login_page.click'].split('>')
        print(locateType, locateExpression)
        click = self.wait.until(lambda x: x.find_element(by=locateType, value=locateExpression))
        return click

    def getUserName(self):
        locateType, locateExpression = self.login_iteim['login_page.username'].split('>')
        usreName = self.wait.until(lambda x: x.find_element(by=locateType,value = locateExpression))
        return usreName

    def getPassword(self):
        locateType, locateExpression = self.login_iteim['login_page.password'].split('>')
        password = self.wait.until(lambda x: x.find_element(by=locateType,value = locateExpression))
        return password

    def getLoginButton(self):
        locateType,locateExpression = self.login_iteim['login_page.loginbutton'].split('>')
        loginbutton = self.wait.until(lambda x: x.find_element(by=locateType,value = locateExpression))
        return loginbutton

    def login(self):
        self.driver.switch_to.frame(self.getFrame())
        time.sleep(2)
        self.getclick().click()
        self.getUserName().send_keys('3031371046')
        self.getPassword().send_keys('zzz284117')
        self.getLoginButton().click()
        self.driver.switch_to.default_content()  # 切换到最上层
        time.sleep(5)



if __name__ == '__main__':
     driver = webdriver.Chrome()
     driver.get('https://mail.qq.com/')
     login = LoginPage(driver)
     login.login()


