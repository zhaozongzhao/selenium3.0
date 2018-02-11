from Common.BasePage import BasePage
from selenium.webdriver.common.by import By

class Home_Page(BasePage):
    #首页 - tab
    home_homeTab_locator= "//a[text()='首页']"
    # 首页 - 我的帐户链接
    home_userInfoLink_locator = '//a[@href="/Member/index.html"]'
    # 首页 - 抢投标按钮 - 第一个
    home_firstBidGrab_locator = '//*[text()="抢投标"]'


    # 默认选第一标进行投资
    def click_firstgrabButton(self):
        self.find_element(By.XPATH, self.home_firstBidGrab_locator, 30).click()

    #获取当前登陆的用户名昵称
    def get_nickname(self):
        return self.find_element(By.XPATH,self.home_userInfoLink_locator,40).text

    #点击用户名昵称 - 进入个人信息页面
    def click_userLink(self):
        userlink = self.find_element(By.XPATH,self.home_userInfoLink_locator,10)
        self.element_scrollIntoView(userlink)
        userlink.click()
