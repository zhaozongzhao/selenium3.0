from common.Basepage import BasePage
from selenium.webdriver.common.by import By
import time
from testDats import  webData as WB


class Login_page_object(BasePage):
    """
    user_input_loc 用户名输入框
    pass_input_loc  密码输入框
    submit_button_loc 确当按钮

    """

    user_input_loc = '//*[@id="react-app-root"]/div/div[2]/div[2]/div[2]/form/div[1]/div/div/span/input'

    pass_input_loc = '//*[@id="react-app-root"]/div/div[2]/div[2]/div[2]/form/div[2]/div/div/span/input'

    submit_button_loc = '//*[@id="react-app-root"]/div/div[2]/div[2]/div[2]/form/div[3]/div/div/button'

    prompt_span =  '/html/body/div[2]/div/span/div/div/div/span'





    #用户名输入框
    def user_input(self,username):
        self.driver.find_element(By.XPATH,self.user_input_loc).send_keys(username)

    #密码收入框
    def  password_input(self,password):
        self.driver.find_element(By.XPATH,self.pass_input_loc).send_keys(password)


    def login_input(self):
        self.driver.find_element(By.XPATH,self.submit_button_loc).click()

    def get_prompt(self):
        time.sleep(1)
        print('开始取值')
        text = self.driver.find_element(By.XPATH,self.prompt_span).text
        return text

    #登陆操作
    def login_button(self,user,password):
        self.driver.get(WB.web_url)
        time.sleep(3)
        self.user_input(user)
        time.sleep(3)
        self.password_input(password)
        self.login_input()









