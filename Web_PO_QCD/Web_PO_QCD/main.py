import unittest

from Common import config
from Common import logger2

#测试套件
s = unittest.TestSuite()
ts = unittest.TestLoader()
s.addTests(ts.discover(config.base_dir + "/TestCases"))

#html测试报告
from HTMLTestRunner import HTMLTestRunner
runner=HTMLTestRunner(output= config.report_dir,report_title="前程贷- web自动化测试报告")
runner.run(s)