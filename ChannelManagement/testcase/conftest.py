
from selenium import webdriver
import pytest
from  Pageobject import Login_page as LD
from  testDats import login_data as TD

@pytest.fixture
def start():
    driver = webdriver.Chrome()
    yield driver

@pytest.fixture()
def login():
    print('开始登陆操作')
    driver = webdriver.Chrome()
    login1 = LD.Login_page_object(driver)
    login1.login_button(TD.login_user_success,TD.login_password_success)
    print('登陆完成')
    return driver

