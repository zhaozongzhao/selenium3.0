
from PageObject.addressbookPage import *
from  selenium import webdriver

def add_contact(driver,name,email,phone):


    addressbook = Addressbook_Page(driver)
    driver.switch_to.default_content()
    addressbook.get_address_book().click()
    driver.switch_to.frame(addressbook.getFrame())
    time.sleep(2)
    addressbook.create_address_book().click()
    addressbook.create_name_address().send_keys(name)
    addressbook.create_email_address().send_keys(email)
    addressbook.create_phone_address().send_keys(phone)
    addressbook.save_button_address().click()


