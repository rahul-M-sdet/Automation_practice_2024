from selenium import webdriver
from selenium.webdriver.chrome.service import Service

srv_obj = Service("C:/Users/RAHUL/Downloads/ChromeSetup.exe")
driver = webdriver.Chrome()
driver.get("http://www.google.co.in/")
