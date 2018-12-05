from  selenium import  webdriver
import random


driver = webdriver.Firefox()
driver.get('http://testmanage.xinyuezx.cn/yueke/admin/main')
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('admin123')
driver.find_element_by_xpath()
