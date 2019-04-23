from selenium import webdriver
import unittest,time

class TestDemo(unittest.TestCase):

    def setUp(self):
    #创建chrome配置对象实例
     chromeoptins = webdriver.ChromeOptions()
    #设定下载文件的路径为'c:\\iDownload' 如果文件不存在则创建
     prefs = {"download.default_directory":'c:\\iDownload'}
    #将自定义地址添加到配置对象的实例中
     chromeoptins.add_experimental_option('prefs',prefs)
     self.driver = webdriver.Chrome(chrome_options=chromeoptins)

    def test_downloadFileByChrome(self):
        url = 'http://pypi.python.org/pypi/selenium'
        self.driver.get(url)
        self.driver.find_element_by_link_text('selenium-3.0.2.tar.gz').click()
        time.sleep(100)

    def tearDown(self):
        self.driver.quit()