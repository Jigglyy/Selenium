import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def init_driver():
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.maximize_window()
    yield driver

    driver.quit()