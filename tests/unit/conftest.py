import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")  # Replace with your actual login URL
    yield driver
    driver.quit()