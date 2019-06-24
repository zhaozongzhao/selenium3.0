from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest,time
from HTMLTestRunner import HTMLTestRunner

class SeleniumGridTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Remote(
            command_executor='http://192.168.0.104:6655/wd/hub',
            desired_capabilities={
                "browserName": "chrome",
                "version": '75.0.3770.100',
                "video": "true",
                "platform": "MAC",
                'javascriptEnable': True
            }

        )
        self.driver.implicitly_wait(30)

    def testSogou(self):
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        assert '百度' in self.driver.title
        print('done')

    def tearDown(self):
        self.driver.quit()

def suite():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(SeleniumGridTest)
    return  unittest.TestSuite(suite1)

def run(suite,report = 'F:\gitstorehouse\selenium3.0\分布式执行验证\selenium.html'):
    with open(report,'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title=u'分布式测试结果',
            description=u'测试报告描述'
        )
        runner.run(suite)



if __name__ == '__main__':
    run(suite())
