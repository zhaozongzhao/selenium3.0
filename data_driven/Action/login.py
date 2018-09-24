from  data_driven.PageObject.LoginPage import *

from selenium import webdriver

def login(driver,userename,passord):

    lp = LoginPage(driver)
    driver.switch_to.frame(lp.getFrame())
    lp.getclick().click()
    lp.getUserName().send_keys(userename)
    lp.getPassword().send_keys(passord)
    lp.getLoginButton().click()
    lp.driver.switch_to.default_content()
    time.sleep(3)



if __name__ == '__main__':
    #册数代码
    driver =  webdriver.Chrome()
    driver.get('https://mail.qq.com/')
    login(driver,'3031371046','zzz284117')