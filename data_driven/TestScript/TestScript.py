from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback #捕获并打印异常
from  data_driven.PageObject.LoginPage import *
from  data_driven.PageObject.addressbookPage import *
from  data_driven.Action.add_contact import *
from  data_driven.Action.login import  *

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
wait = WebDriverWait(driver, 10, 0.2)
login(driver,'3031371046','zzz284117')
add_contact(driver,'中岛一','2206321864@qq.com','18301565568')
driver.quit()

