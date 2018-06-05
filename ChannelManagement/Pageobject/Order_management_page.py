from common.Basepage import BasePage
from selenium.webdriver.common.by import By
import time


class Order_management(BasePage):

   #搜索框
   search_input_loc = '//*[@id="layout"]/div[1]/div/div/div/div[2]/div/span/input'

   #查询按钮
   query_button_loc = '//*[@id="layout"]/div[1]/div/div/div/div[2]/div/span/span/button'

   #租户名称
   customer_loc='//*[@id="layout"]/div[1]/div/div/div/div[3]/div[1]/div[1]/div[1]/span'


   #创建时间
   create_time_loc = '//*[@id="layout"]/div[1]/div/div/div/div[3]/div[1]/div[2]/div[1]/span[2]'


   #订单id
   order_id_loc = '//*[@id="layout"]/div[1]/div/div/div/div[3]/div[1]/div[2]/div[2]/span[2]'

   #客户合同号
   customer_cintract_loc = '//*[@id="layout"]/div[1]/div/div/div/div[3]/div[1]/div[2]/div[3]/span[2]'

   #销售员
   salesman_loc = '//*[@id="layout"]/div[1]/div/div/div/div[3]/div[1]/div[2]/div[4]/span[2]'


   #订单状态
   order_type_loc = '//*[@id="layout"]/div[1]/div/div/div/div[3]/div[1]/div[2]/div[5]/span[2]'

   #总价
   total_price_loc = '//*[@id="layout"]/div[1]/div/div/div/div[3]/div[1]/div[2]/div[6]/span[2]'


   #订单总数
   order_sum_loc = '//*[@id="layout"]/div[1]/div/div/div/div[13]/ul/li[1]'


   #上一页
   previous_page_loc = '//*[@id="layout"]/div[1]/div/div/div/div[6]/ul/li[2]/a'

   #下一页
   next_page_loc = '//*[@id="layout"]/div[1]/div/div/div/div[6]/ul/li[4]/a'

   #订单输入框输入
   def search_input(self,information):
       self.driver.find_element(By.XPATH,self.search_input_loc).send_keys(information)


   def query_button(self):
       self.driver.find_element(By.XPATH,self.query_button_loc).click()


   def get_order_type(self):
      self.driver.find_element(By.XPATH,self.order_type_loc).text


   def get_total_price(self):
      self.driver.find_element(By.XPATH,self.total_price_loc).text


   def get_order_id(self):
      self.driver.find_element(By.XPATH,self.order_id_loc).text


   def get_customer_cintract(self):
      self.driver.find_element(By.XPATH,self.customer_cintract_loc).text

   #获取销售员
   def get_salesman(self):
      self.driver.find_element(By.XPATH,self.salesman_loc).text


   #订单总数
   def get_order_sum(self):
      time.sleep(5)
      ordersum =  self.driver.find_element(By.XPATH,self.order_sum_loc).text
      return ordersum

   #获取销售员
   def get_customer(self):
      return self.driver.find_element(By.XPATH,self.customer_loc).text


   #查询操作
   def query_operation(self,information):
      self.search_input(information)
      self.query_button()
