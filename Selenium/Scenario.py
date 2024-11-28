# lanuch the browser , hit the url and
# there is some table with row column and verify the text inside the cell which matches the input
# string and return the row and column numbers


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("xyz")  # launch the url
driver.maximize_window()
driver.id .sendkeys() # enter the username
driver.id.send # enter the password
driver.id.click()  # submit button

str='xyz'

# first i have to identify the table
#

# Consider the list with intiger and char, create the seperate list for both integer and char
