  import pytest
from Pageobject.Login_page import Login_page_object
from testDats import login_data as LD
from common import logger_creat


@pytest.mark.userfixtures('start')
class TestUserPassword(object):

    def setup_class(cls):
        cls.logger = logger_creat.loggingcreate()

    def setup(self):
        self.logger.info('###################开始执行测试###########################')

    def teardown(self):
        self.logger.info('###################测试执行结束###########################')
        self.log.driver.close()



    @pytest.mark.smoke
    def test_user_success(self,start):
        self.log = Login_page_object(start)
        self.logger.info('测试模块   test_user_success')
        self.logger.info('输入的的登陆信息 用户名:{}, 密码:{}'.format(LD.login_user_success,LD.login_password_success))
        self.log.login_button(user=LD.login_user_success,password=LD.login_password_success)

    @pytest.mark.smoke
    def test_user_null(self,start):
        self.log = Login_page_object(start)
        self.logger.info('测试模块   test_user_null')
        self.logger.info('输入的的登陆信息 用户名:{}, 密码:{}'.format(LD.login_null_user_info,LD.login_password_success))
        self.log.login_button(user=LD.login_null_user_info,password=LD.login_password_success)
        self.logger.info('返回提示语句:{}'.format(self.log.get_prompt()))
        assert self.log.get_prompt() == '登录名不能为空'

    @pytest.mark.smoke
    def test_password_null(self,start):
        self.log = Login_page_object(start)
        self.logger.info('测试模块   test_password_null')
        self.logger.info('输入的的登陆信息 用户名:{}, 密码:{}'.format(LD.login_user_success,LD.login_null_password_info))
        self.log.login_button(user=LD.login_user_success,password=LD.login_null_password_info)
        self.logger.info('返回提示语句:{}'.format(self.log.get_prompt()))
        assert  self.log.get_prompt() == '密码名不能为空'





if __name__ == '__main__':
    pytest.main()

