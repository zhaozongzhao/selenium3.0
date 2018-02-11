from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class BidInfo_Page(BasePage):

    #标名
    bid_name_locator = '//span[text()="%s"]'
    # 标详情页面 - 投资金额输入处
    bid_moneyInput_locator = '//input[@data-url="/Invest/invest"]'
    # 标详情页面 - 投标按钮
    bid_moneySubmit_locator = "//button[text()='投标']"
    # 投资成功 - 弹出框 - 激活并查看按钮
    bid_sucess_popup_button_locator = '//div[@class="layui-layer-content"]//button'
    #投资不成功 - 弹出框 - 消息内容
    bid_failed_popup_message_locator= "//*[contains(@class,'layui-layer-dialog')]//*[@class='text-center']"


    # 标详情页面 - 找到投资金额输入处 - 输入金额  - 确认投资
    def investment_action_getInvestTime(self,bid_money):
        # 投资 - 金额
        bid_moneyInput_ele = self.find_element(By.XPATH,self.bid_moneyInput_locator,40)
        self.element_scrollIntoView(bid_moneyInput_ele)
        bid_moneyInput_ele.send_keys(bid_money)
        # 提交投资操作
        bid_moneySubmit_ele = self.find_element(By.XPATH,self.bid_moneySubmit_locator)
        self.element_scrollIntoView(bid_moneySubmit_ele)
        # 获取当前时间 - 包括日期 和 时间
        obj_date_time = time.strftime('%Y-%m-%d %H:%M')
        print("投资时间：", obj_date_time, ",投资金额：", bid_money)
        #点击投资按钮
        bid_moneySubmit_ele.click()
        return obj_date_time

    # 投资成功 - 提示框 - 点击激活和查看按钮
    def click_success_investPop_button(self):
        # 点击激活并查看 - 进入个人页面
        self.find_element(By.XPATH,self.bid_sucess_popup_button_locator,40).click()
        time.sleep(1)

    # 在投资之前，获取投资时用户可用的余额
    def get_user_moneyLeft(self):
        return self.find_element(By.XPATH,self.bid_moneyInput_locator,40).text

    #投资不成功 - 获取提示框中的提示信息
    def get_popUp_message(self):
       return self.find_element(By.XPATH,self.bid_failed_popup_message_locator,20).text






