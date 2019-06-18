from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Remote(
    command_executor="http://172.168.50.115:7778/wd/hub",
    desired_capabilities= {
        "browserName" : 'chrome',
        "video": 'true',
        'platform':'MAC'
    }

)
driver.get('http://www.baidu.com')
time.sleep(3)
