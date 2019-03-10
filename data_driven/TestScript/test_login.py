import pytest
from Action import login
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback #捕获并打印异常
from  PageObject.LoginPage import *
from  PageObject.addressbookPage import *
from  Action.add_contact import *
from  Action.login import  *
from  Util.Excel import *
from  Util.log import *
import pytest
from PageJectVar import var

class Test_login:


    def test_login(self):
        driver = webdriver.Chrome()
        driver.get('https://mail.qq.com/')
        pe =  parseExcel(Excelobject_path) #实调例化excel调用
        pe.set_sheet_by_name('登陆账号') #打开sheet页
        info('当前sheet页'+pe.get_sheet_name())
        rows = pe.get_all_rows()[1:]
        info('当前的所有行'+str(rows))
        for id,row in enumerate(rows):
            if row[4].value == 'y':
               username =row[1].value
               password =row[2].value
               info('登陆用户名和密码'+str(username)+'   '+str(password))
               login(driver,username,password)