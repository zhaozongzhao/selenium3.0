from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback

class Addressbook_Page(object):

    def __init__(self,driver):
        self.driver = driver

    def addressbook(self):
        try:
            wait = WebDriverWait(self.driver, 10, 0.2)
            address_book = wait.until(lambda x: x.find_element_by_xpath('//*[@id="navBarTd"]/li[3]/a'))
            address_book.click()
            self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="mainFrame"]'))

            add_button = wait.until(lambda x: x.find_element_by_xpath('//*[@id="bar"]/div/div[1]/div[2]/a[1]'))
            add_button.click()
            create_name = wait.until(
                lambda x: x.find_element_by_xpath('//*[@id="con"]/div/div/ul/li[1]/div/span[1]/input'))
            create_name.send_keys('中岛一')
            create_email = wait.until(lambda x: x.find_element_by_xpath('//*[@id="con"]/div/div/ul/li[2]/div/input'))
            create_email.send_keys('2206321864@qq.com')
            create_phone = wait.until(lambda x: x.find_element_by_xpath('//*[@id="con"]/div/div/ul/li[3]/div/input'))
            create_phone.send_keys('16619854117')
            save_button = wait.until(lambda x: x.find_element_by_xpath('//*[@id="bar"]/div/div/a[1]'))
            save_button.click()
            self.driver.switch_to.default_content()
            out_button = wait.until(lambda x: x.find_element_by_xpath('//*[@id="SetInfo"]/div[1]/a[3]'))
            out_button.click()

        except Exception as e:
            print(traceback.print_exc(e))

