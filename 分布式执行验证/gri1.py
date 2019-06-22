from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Remote(
    command_executor="http://192.168.0.100:6655/wd/hub",
    desired_capabilities= {
        "browserName" : 'chrome',
        "video": 'true',
         'platform': 'WINDOWS',
         'platformName': 'WINDOWS'
    }

)

# time.sleep(3)
# from selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.baidu.com')
# driver.save_screenshot('ceshi1.png')

# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')