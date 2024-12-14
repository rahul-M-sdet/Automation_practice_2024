from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME, "Password").send_keys("admin")
driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()

Act_title = driver.title
Expec_title = "Your store. Login"

if Act_title == "Your store. Login":
    driver.close()
