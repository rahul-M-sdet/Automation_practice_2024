import pytest
from selenium import webdriver

driver = None


@pytest.fixture()
def setup():
    global driver
    driver = webdriver.chrome
    #driver.maximise_window
    print("Start the browser")
    yield
    driver.quit()
    print("close the browser")


def test_1(setup):
    driver.get("https://www.facebook.com")
    print("Test 1 executed")


def test_2(setup):
    driver.get("https://www.google.com")
    print("Test 2 executed")


def test_3(setup):
    driver.get("https://www.gmail.com")
    print("Test 3 executed")
