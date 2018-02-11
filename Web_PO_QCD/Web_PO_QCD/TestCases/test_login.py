import unittest
from selenium import webdriver

from PageObjects.login_page import Login_Page
from PageObjects.home_page import Home_Page

from testdata import login_testdata as TD
from testdata import COMM_DATA as CD
import logging

class Test_Login(unittest.TestCase):



    def setUp(self):
        logging.info("========start test login=========")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.loginpage = Login_Page(self.driver)
        self.verificationErrors = []
    def tearDown(self):
        logging.info("========end test login=========")
        self.driver.close()
        self.driver.quit()


    def test_login_ok(self):
        logging.info("测试用例：正常登陆前程贷。")
        #登陆
        self.loginpage.login(CD.web_url,TD.login_username_ok,TD.login_passwd_ok)
        #校验
        homepage = Home_Page(self.driver)
        self.assertIn(TD.check_nickname,homepage.get_nickname())


    def test_login_noUsername(self):
        logging.info("测试用例：异常用例 - 用户名为空")
        # 登陆
        self.loginpage.login(CD.web_url,"",TD.login_passwd_ok)
        #校验
        self.assertEqual(TD.check_noUser_info,self.loginpage.get_wrong_info())


    def test_login_noPasswd(self):
        logging.info("测试用例：异常用例 - 密码为空")
        # 登陆
        self.loginpage.login(CD.web_url,TD.login_username_ok,"")
        #校验
        self.assertEqual(TD.check_noPasswd_info,self.loginpage.get_wrong_info())

