import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

srv_obj = Service("C:/Users/RAHUL/Downloads/ChromeSetup.exe")
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get('https://www.flipkart.com/')
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@type='text']").send_keys('mack')
time.sleep(10)
lst_options = driver.find_elements(By.XPATH, "//div[@class='YGcVZO _2VHNef']")
print(len(lst_options))
for e1 in lst_options:
    print(e1.text)
    time.sleep(5)
    if e1 == 'macbook air m3':
        e1.click()
