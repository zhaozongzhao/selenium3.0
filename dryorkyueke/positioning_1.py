from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

# driver.find_element_by_id('kw').send_keys('12345678')
# sleep(5)
driver.find_element(by='id',value='kw').send_keys('123456789')