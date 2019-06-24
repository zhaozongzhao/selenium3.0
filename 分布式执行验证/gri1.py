from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Remote(
    command_executor="http://192.168.0.102:5555/wd/hub",
    desired_capabilities= {
        "browserName" : "chrome",
        "version" : '75.0.3770.100',
        "video": "true",
        "platform": "MAC",
        'javascriptEnable':True
    }

)
driver.get('http://www.baidu.com')
time.sleep(5)
assert '百度' in driver.title
driver.quit()


