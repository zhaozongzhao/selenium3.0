import pytest
from common import logger_creat
from Pageobject.menu_page import menu_page_object
from Pageobject.Order_management_page import Order_management as OR
import time
from testDats import order_data as OD


@pytest.mark.userfixtures('login')
class Testorder(object):

    def setup_class(cls):
        cls.logger = logger_creat.loggingcreate()

    def setup(self):
        self.logger.info('###################开始执行测试###########################')


    def teardown(self):
        self.logger.info('###################测试执行结束###########################')
        self.OR.driver.close()


    # @pytest.mark.order
    def test_order_sum(self,login):
        '''获取订单数量'''
        self.logger.info('进入订单管理界面')
        time.sleep(3)
        self.OR = OR(login)
        sum = self.OR.get_order_sum()
        self.logger.info('获取的订单数量{}== {}'.format(sum,OD.succeed_sum))
        assert sum == OD.succeed_sum

    # @pytest.mark.order
    def test_query_success(self,login):
        self.OR = OR(login)
        time.sleep(5)
        id = self.OR.get_order_id()
        customername = self.OR.get_customer()
        create_time = self.OR.get_create_time()
        order_type = self.OR.get_order_type()
        self.logger.info('获取订单id{},项目名称{},创建时间{},订单状态{}'.format(id,customername,create_time,order_type))
        self.logger.info('测试数据中id{},项目名称{},创建时间{},订单状态{}'.format(OD.succeed_id,OD.succeed_name,
                                                                 OD.succeed_time,OD.succeed_type))
        assert id ==  OD.succeed_id
        assert customername == OD.succeed_name
        assert create_time == OD.succeed_time
        assert order_type == OD.succeed_type


    @pytest.mark.order1
    def test_help_success(self,login):
         self.OR = OR(login)
         time.sleep(5)
         list = self.OR.help_input()
         self.logger.info(list)
         self.OR.driver.switch_to_window(list[0])
         time.sleep(10)

if __name__ == '__main__':
    pytest.main(["-m order1","--html=HtmlReport/smoke_report.html"])
