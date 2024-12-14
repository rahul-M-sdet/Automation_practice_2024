import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

srv_obj = Service("C:/Users/RAHUL/Downloads/ChromeSetup.exe")
driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
options = driver.find_elements(By.XPATH, "//label[@class='form-check-label' and contains(text(),'day')]")
print(len(options))
for op1 in options:
    op1.click()
    if op1.is_selected():
        time.sleep(10)
        op1.click()
