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
from PageJectVar import var

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
pe =  parseExcel(Excelobject_path)
# wait = WebDriverWait(driver, 10, 0.2)
pe.set_sheet_by_name('登陆账号')
print(pe.get_sheet_name())
rows = pe.get_all_rows()[1:]
for id,row in enumerate(rows):
    if row[4].value == 'y':
        username =row[1].value
        password =row[2].value
        print(username,password)
        try:
            login(driver,username,password)

            pe.set_sheet_by_name('联系人')
            print(pe.get_sheet_name())
            rows1 =  pe.get_all_rows()[1:]
            print('所有行',rows1)

            for id1,row in enumerate(rows1):
                if row[4].value == 'y':
                    try:
                       add_contact(driver,row[1].value,row[2].value,row[3].value)
                       pe.write_cell_content_time(id1+2,6)
                       pe.write_cell_content(id1+2,7,'pass')
                    except Exception as e:
                       pe.write_cell_content(id1+2,6,'fail')
                else:
                    pe.write_cell_content(id1+2,6,'忽略')

        except Exception as a:
            pe.set_sheet_by_name('登陆账号')
            pe.write_cell_content(id+2,6,'fail')

    else:
         pe.set_sheet_by_name('登陆账号')
         pe.write_cell_content(id+2,6,'忽略')
         pe.write_cell_content_time(id+2,7)
         continue







# login(driver,'3031371046','zzz284117')
# add_contact(driver,'中岛一','2206321864@qq.com','18301565568')
# driver.quit()

