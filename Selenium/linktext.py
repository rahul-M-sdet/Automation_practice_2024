from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

# tagname and class

# Ttl_links = driver.find_elements(By.TAG_NAME, "a")
# print(len(Ttl_links))


# class

product=driver.find_elements(By.CLASS_NAME,"product-page-size")
print(len(product))


