from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from common import config



class BasePage:

      def __init__(self,driver):
          self.driver = driver


      #等待元素可见
      def element_wait(self,by,locator,wait_time=5):
          if by not in [By.CLASS_NAME,By.ID,By.XPATH,By.LINK_TEXT,By.NAME,By.CSS_SELECTOR]:
              raise NameError('请输入正确的目标元素')
          WebDriverWait(self.driver,wait_time,0.5).until(EC.visibility_of_element_located(by,locator))


      #将元素滚动到可见区域
      def element_scrollIntoView(self,ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        time.sleep(0.5)


      #查找元素
      def find_element(self,by,locator,wait_time=5):
        self.driver.element_wait(by,locator,wait_time)
        return self.driver.find_element(by,locator)


      # 截图
      def save_img(self, img_name):
         # logging.info("截图位置：{}" (config.image_dir + img_name))
         self.driver.save_screenshot(config.image_dir + img_name)


      #打开网址
      def open_url(self,url):
          self.driver.get(url)

      #接收alert
      def title_alert(self):
        '''接收alert'''
        h=self.driver.switch_to_alert().text
        self.driver.switch_to_alert().dismiss()
        return  h


