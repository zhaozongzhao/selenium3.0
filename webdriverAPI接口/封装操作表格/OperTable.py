from selenium import webdriver
import unittest
import time
from webdriverAPI接口.封装操作表格.Table import Table

class TestTableOpertion(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testTable(self):
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\封装表格验证.html'
        self.driver.get(url)
        webTable = self.driver.find_element_by_tag_name('table')
        table = Table(webTable)
        print(table.getRowCount())
        print(table.getColumnCount())
        cell = table.getCell(2,3)
        self.assertAlmostEqual('第二行第三列',cell.text)
        cellinput = table.getWebElementInCell(3,2,'tag name','input')
        cellinput.send_keys('测试')
        time.sleep(3)
# 测试数据

if __name__ == '__mian__':
    unittest.main()
    print('验证数据')