import unittest
from selenium import webdriver

from PageObjects.login_page import Login_Page
from testdata import COMM_DATA as CD
from PageObjects.home_page import Home_Page
from PageObjects.bidInfo_page import BidInfo_Page
from PageObjects.userInfo_page import UserInfo_Page
from testdata import investment_testdata as TD
import logging

import datetime

class Test_Investment(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        loginpage = Login_Page(self.driver)
        loginpage.login(CD.web_url, CD.login_username, CD.login_passwd)
        self.verificationErrors = []

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


    def test_investment_normal(self):
        logging.info("测试用例：投资成功-从首页进入标页面，在标详情页面进行投资")
        #在首选标 - 点击抢投标 - 进入标详情页面
        homepage = Home_Page(self.driver)
        homepage.click_firstgrabButton()
        #标详情页面 - 进行投资操作
        bidinfo_page = BidInfo_Page(self.driver)
        user_leftMoney_beforeInvs = bidinfo_page.get_user_moneyLeft()
        invest_dateAndTime = bidinfo_page.investment_action_getInvestTime(TD.money_right)
        #投资成功 - 弹出框 - 点击激活并查看按钮 - 进入个人页面
        bidinfo_page.click_success_investPop_button()

        #结果校验
        #个人信息页面 - 获取投资记录
        userinfo_page = UserInfo_Page(self.driver)
        userinfo_page.display_investment_projects()
        investRecord_dateAndTime = userinfo_page.get_firstInvestRecord_dateAndTime()
        #时间格式转换
        invest_datetime = datetime.datetime.strptime(invest_dateAndTime,"%Y-%m-%d %H:%M")
        investRecord_datetime = datetime.datetime.strptime(investRecord_dateAndTime,"%Y-%m-%d %H:%M")
        print("***********************************")
        print(invest_datetime)
        print(investRecord_datetime)
        print("***********************************")
        #断言
        differ = (investRecord_datetime - invest_datetime).seconds
        print(differ)
        self.assertLessEqual(differ,60)

        #获取用户当前剩余的金额 - 用户所剩余额确认
        user_leftmoney_afterInves = userinfo_page.get_moneyLeft()
        self.assertEqual(user_leftmoney_afterInves,int(user_leftMoney_beforeInvs)-int(TD.money_right))


    def test_invest_no100(self):
        logging.info("测试用例：投资异常用例-投资金额不是100的整数倍。")
        # 在首选标 - 点击抢投标 - 进入标详情页面
        homepage = Home_Page(self.driver)
        homepage.click_firstgrabButton()
        # 标详情页面 - 进行投资操作
        bidinfo_page = BidInfo_Page(self.driver)
        bidinfo_page.investment_action_getInvestTime(TD.money_no100)
        #校验
        #获取报错提示
        self.assertEqual(bidinfo_page.get_popUp_message(),TD.check_wrongMoney)
