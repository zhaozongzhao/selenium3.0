from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback #捕获并打印异常
from  data_driven.PageObject.LoginPage import *
from  data_driven.PageObject.addressbookPage import *
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
wait = WebDriverWait(driver, 10, 0.2)
lp = LoginPage(driver)
addressbook = Addressbook_Page(driver)

try:
    lp.login()
    addressbook.addressbook()

except Exception as e:
    traceback.print_exc(e)
finally:
    driver.close()
    print('运行结束')