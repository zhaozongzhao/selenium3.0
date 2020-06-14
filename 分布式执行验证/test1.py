from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = webdriver.ChromeOptions()
chrome_options = Options()
options.binary_location = r"/Applications/派药房.app/Contents/MacOS/派药房"
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path='/Users/zhaozongzhao/Downloads/chromedriver', options=options,
                          port=9515)
# driver = webdriver.Chrome(executable_path='/Users/zhaozongzhao/Downloads/chromedriver', options=options,
#                           chrome_options=chrome_options, port=9515)

title = '//*[@id="login_index"]/div/div[2]/div'
sleep(3)

driver.quit()
# driver.close()
