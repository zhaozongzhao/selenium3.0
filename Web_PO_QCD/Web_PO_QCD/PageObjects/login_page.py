from Common.BasePage import BasePage
from selenium.webdriver.common.by import By


class Login_Page(BasePage):
    #用户名
    login_username_locator = "//*[@name='phone']"
    #密码
    login_passwd_locator = "//*[@name='password']"
    #登陆按钮
    login_button_locator = "//button"
    #用户名不是11位/密码为空的提示信息
    login_wrongInfo_locator = '//div[@class="form-error-info"]'
    #用户名和密码都有，但是登陆失败的提示(在页面中间弹出的提示框)：
    login_wrong_centerInfo_locator = "//div[@class='layui-layer-content']"

    #登录功能
    def login(self, url, username, passwd):
        self.driver.get(url)
        self.find_element(By.XPATH,self.login_username_locator).send_keys(username)
        self.find_element(By.XPATH,self.login_passwd_locator).send_keys(passwd)
        #是否勾选 记住用户名 - 没有勾选则勾选
        js = 'var a = document.getElementsByName("remember_me")[0];return a.checked;'
        checked_value = self.driver.execute_script(js)
        if checked_value == False:
            self.find_element(By.NAME,"remember_me").click()
        #点击登陆
        self.find_element(By.XPATH,self.login_button_locator).click()


    # 用户名不是11位/密码为空的提示信息（直接在输入框下边的提示）
    def get_wrong_info(self):
        return self.find_element(By.XPATH,self.login_wrongInfo_locator).text


    # 用户名和密码都有，但是登陆失败的提示(在页面中间弹出的提示框)：
    def get_wrong_centerInfo(self):
        return self.find_element(By.XPATH,self.login_wrong_centerInfo_locator).text



