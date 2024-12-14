from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains


srv_obj = Service("C:/Users/RAHUL/Downloads/ChromeSetup.exe")
driver = webdriver.Chrome()
driver.get("https://www.practo.com/hyderabad/ear-nose-throat-ent-specialist/miyapur")
driver.maximize_window()

buttons=driver.find_elements(By.XPATH,"//button[@data-qa-id='book_button']")
for btn in buttons:
    if btn.text='Dr. Sathish Kumar S':
         btn.click()
