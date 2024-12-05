import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


srv_obj = Service("C:/Users/RAHUL/Downloads/ChromeSetup.exe")
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# mouse action
time.sleep(5)
source=driver.find_element(By.XPATH,"//div[@id='draggable']")
Target=driver.find_element(By.XPATH,"//div[@id='droppable']")

act=ActionChains(driver)
act.drag_and_drop(source,Target).perform()
act.move_to_element(driver.find_element(By.XPATH,"//button[@class='dropbtn']")).perform()





