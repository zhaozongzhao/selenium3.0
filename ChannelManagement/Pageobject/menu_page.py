from common.Basepage import BasePage
from selenium.webdriver.common.by import By

class menu_page_object(BasePage):

    #订单管理
    order_management_loc = '//*[@id="sidebar-menu"]/ul/li[1]'

    #服务管理
    service_management_loc = '//*[@id="sidebar-menu"]/ul/li[2]'

    #资金账户
    capital_account_loc = '//*[@id="sidebar-menu"]/ul/li[3]'


    def order_management_button(self):
        self.driver.find_element(By.XPATH,self.order_management_loc).click()

    def service_management_button(self):
        self.driver.find_element(By.XPATH,self.service_management_loc).click()

    def capital_account_button(self):
        self.driver.find_element(By.XPATH,self.capital_account_loc)
