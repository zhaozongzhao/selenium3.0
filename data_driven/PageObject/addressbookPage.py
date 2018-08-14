from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from  data_driven.PageJectVar import var
from data_driven.Util import ParsePageObjectRepository
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback

class Addressbook_Page(object):

    def __init__(self,driver):
        self.driver = driver
        self.paser_page_object = ParsePageObjectRepository.ParsePageObjectRepository(var.PaserPageObject_path)
        self.addressbook_iteim = self.paser_page_object.getItemSection('qqmail_homepage')
        print(self.addressbook_iteim)
        self.wait = WebDriverWait(self.driver,10,0.2)



    def get_address_book(self):
        locateType,locateExpression  =  self.addressbook_iteim['get_address_book'].split('>')
        address_book = self.wait.until(lambda x : x.find_element(by=locateType,value = locateExpression))
        return address_book

    def getFrame(self):
        locateType,locateExpression  =  self.addressbook_iteim['getframe'].split('>')
        frame = self.wait.until(lambda x : x.find_element(by=locateType,value = locateExpression))
        return frame

    def create_address_book(self):
        locateType,locateExpression  =  self.addressbook_iteim['create_address_book'].split('>')
        add_button =self.wait.until(lambda x : x.find_element(by=locateType,value = locateExpression))
        return add_button

    def create_name_address(self):
        locateType,locateExpression  =  self.addressbook_iteim['create_name_address'].split('>')
        create_name  = self.wait.until(lambda x : x.find_element(by=locateType,value = locateExpression))
        return create_name

    def create_email_address(self):
        locateType,locateExpression  =  self.addressbook_iteim['create_email_addres'].split('>')
        create_email  = self.wait.until(lambda x : x.find_element(by=locateType,value = locateExpression))
        return create_email

    def create_phone_address(self):
        locateType,locateExpression  =  self.addressbook_iteim['create_phone_address'].split('>')
        create_phone  = self.wait.until(lambda x : x.find_element(by=locateType,value = locateExpression))
        return create_phone

    def save_button_address(self):
        locateType,locateExpression  =  self.addressbook_iteim['save_button_address'].split('>')
        save_button  = self.wait.until(lambda x : x.find_element(by=locateType,value = locateExpression))
        return  save_button

    def out_button_email(self):
        locateType,locateExpression  =  self.addressbook_iteim['out_button_email'].split('>')
        out_button = self.wait.until(lambda x : x.find_element(by=locateType,value = locateExpression))
        return  out_button

    def addressbook(self):
            self.get_address_book().click()
            self.driver.switch_to.frame(self.getFrame())
            time.sleep(2)
            self.create_address_book().click()
            self.create_name_address().send_keys('中岛一')
            self.create_email_address().send_keys('2206321864@qq.com')
            self.create_phone_address().send_keys('18301565568')
            self.save_button_address().click()
            # self.out_button_email().click()


