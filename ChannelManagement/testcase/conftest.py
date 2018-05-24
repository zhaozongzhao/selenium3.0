from selenium import webdriver
import pytest

@pytest.fixture
def start():
    driver = webdriver.Chrome()
    yield driver


