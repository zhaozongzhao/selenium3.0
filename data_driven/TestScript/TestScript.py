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
        try:
            login(driver,username,password)
            pe.write_cell_content_time(id+2,7)
            pe.write_cell_content(id+2,6,'登陆pass')
            pe.set_sheet_by_name('联系人')
            info(pe.get_sheet_name())
            rows1 =  pe.get_all_rows()[1:]
            info('当前的所有行'+str(rows1))

            for id1,row in enumerate(rows1):
                if row[4].value == 'y':
                    try:
                       info('输入信息'+str(row[1].value)+str(row[2].value)+str(row[3].value))
                       add_contact(driver,row[1].value,row[2].value,row[3].value)
                       pe.write_cell_content_time(id1+2,6)
                       pe.write_cell_content(id1+2,7,'pass')
                    except Exception as e:
                       error('执行失败'+str(e))
                       pe.write_cell_content(id1+2,7,'fail')
                       pe.write_cell_content_time(id1+2,6)

                else:
                    pe.write_cell_content(id1+2,7,'忽略')
                    pe.write_cell_content_time(id1+2,6)

            add_out_button(driver)

        except Exception as a:
            error('登陆失败'+str(a))
            pe.set_sheet_by_name('登陆账号')
            pe.write_cell_content(id+2,6,'登陆fail')
            pe.write_cell_content_time(id+2,7)


    else:
         pe.set_sheet_by_name('登陆账号')
         pe.write_cell_content(id+2,6,'登陆忽略')
         pe.write_cell_content_time(id+2,7)
         continue







login(driver,'3031371046','zzz284117')
add_contact(driver,'中岛一','2206321864@qq.com','18301565568')
driver.quit(row[1].value,row[2].value,row[3].value)

