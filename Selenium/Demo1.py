from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive/com/")
driver.find_element(By.NAME, "username").send_keys('Admin')
driver.find_element(By.NAME, 'password').send_keys('admin123')
driver.find_element(By.CLASS_NAME, "btn big-btn primary").click()
title = driver.title
assert OrangeHRM == title
driver.close()
