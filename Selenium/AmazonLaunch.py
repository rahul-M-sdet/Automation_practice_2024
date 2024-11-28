import time
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
driver.maximize_window()
link1 = driver.find_element(By.XPATH, "//span[@class='nav-line-2 ']")
time.sleep(5)
act = ActionChains(driver)
act.move_to_element(link1).perform()
driver.find_element(By.LINK_TEXT,"Sign in").click()
driver.close()
