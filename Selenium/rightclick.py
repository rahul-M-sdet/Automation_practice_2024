import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

srv_obj = Service("C:/Users/RAHUL/Downloads/ChromeSetup.exe")
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
act = ActionChains(driver)
time.sleep(20)
act.context_click(driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")).perform()
