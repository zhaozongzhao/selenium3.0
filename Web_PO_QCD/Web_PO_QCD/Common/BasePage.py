from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

import logging
from Common import config

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    #等待元素可见
    def element_wait(self,by,locator,wait_time=5):
        if by not in [By.ID,By.XPATH,By.LINK_TEXT,By.CSS_SELECTOR,By.CLASS_NAME,By.TAG_NAME,By.PARTIAL_LINK_TEXT]:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
        WebDriverWait(self.driver,wait_time,0.5).until(EC.visibility_of_element_located((by,locator)))

    #将元素滚动到可见区域
    def element_scrollIntoView(self,ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        time.sleep(0.5)

    #查找元素 -
    def find_element(self,by,locator,wait_time=5):
        self.element_wait(by,locator,wait_time)
        return self.driver.find_element(by,locator)

    # 截图
    def save_img(self, img_name):
        logging.info("截图位置：%s" % (config.image_dir + img_name))
        self.driver.save_screenshot(config.image_dir + img_name)