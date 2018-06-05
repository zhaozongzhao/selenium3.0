import pytest
from common import logger_creat
from Pageobject.menu_page import menu_page_object
from Pageobject.Order_management_page import Order_management as OR
import time


@pytest.mark.userfixtures('login')
class Testorder(object):

    def setup_class(cls):
        cls.logger = logger_creat.loggingcreate()

    def setup(self):
        self.logger.info('###################开始执行测试###########################')


    def teardown(self):
        self.logger.info('###################测试执行结束###########################')


    @pytest.mark.order
    def test_order(self,login):
        self.logger.info('进入订单管理界面')
        time.sleep(3)
        self.OR = OR(login)
        sum = self.OR.get_order_sum()
        assert sum == 14




if __name__ == '__main__':
    pytest.main(["-m order","--html=HtmlReport/smoke_report.html"])
