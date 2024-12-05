import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

srv_obj = Service("C:/Users/RAHUL/Downloads/ChromeSetup.exe")
driver = webdriver.Chrome()
time.sleep(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

act = ActionChains(driver)
act.double_click(driver.find_element(By.XPATH,"//button[contains(text(),'Copy Text')]")).perform()

