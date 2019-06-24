# time.sleep(3)
from selenium import webdriver
#无浏览器执行
# from selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.baidu.com')
# driver.save_screenshot('ceshi4.png')

A = {'browserName': 'chrome', 'version': '75.0.3770.100', 'video': 'true', 'platform': 'MAC', 'javascriptEnable': True}
b = {'firstMatch': [], 'alwaysMatch': {}}
b['alwaysMatch']= A.copy()
print(b)
