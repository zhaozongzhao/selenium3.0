from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class UserInfo_Page(BasePage):
    # 个人详情页面 - 我的投资项目tab
    user_investment_projects_tab_locator = "//div[text()='投资项目']"
    # 个人详情页面 - 投资记录列表
    user_investment_table_locator = '//*[@class="deal_manage_list" and contains(@style,"display: block")]//table//tr'
    # 个人详情页面 -  第一条投资记录的日期和时间
    first_investRecord_date_locator = '//div[@ms-html="item.date"]'
    first_investRecord_time_locator = '//div[@ms-html="item.time"]'

    #个人可用余额
    user_moneyLeft_locator = '//*[@class="color_sub"]'


    # 个人详情页面 - 投资项目tab栏点击 - 显示投资列表
    def display_investment_projects(self):
        investment_projects_tab_ele = self.find_element(By.XPATH,self.user_investment_projects_tab_locator,30)
        self.element_scrollIntoView(investment_projects_tab_ele)
        investment_projects_tab_ele.click()
        #等待列表数据呈现
        self.element_wait(By.XPATH,self.user_investment_table_locator,10)
        time.sleep(1)

    #获取第一条投资记录的投资日期和时间
    def get_firstInvestRecord_dateAndTime(self):
        invest_date = self.find_element(By.XPATH,self.first_investRecord_date_locator).text
        invest_time = self.find_element(By.XPATH,self.first_investRecord_time_locator).text
        return invest_date+" "+invest_time

    #获取个人名下帐户余额
    def get_moneyLeft(self):
        return self.find_element(By.XPATH,self.user_moneyLeft_locator,30).text








