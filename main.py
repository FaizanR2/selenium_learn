from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # allows us to use common keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://iulms.iuk.edu.pk/")
print(driver.title)

# Sending a message to a search bar

# search_element = driver.find_element_by_id("sidr")
# search_element.send_keys("test")
# search_element.send_keys(Keys.RETURN)

# driver.clear() # make sure to use this before sending keys again, clears previous input keys if sent to something like a search bar

# Getting entire HTML of page
# print(driver.page_source)

# Explicit wait: waiting a while before page changes so we can get elements, from selenium documentation

# try:
#     test_text = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
# finally:
#     driver.quit()

# time.sleep(3)

test_text = driver.find_element_by_class_name("list__item") # for multiple elements use find_elements_by
print(test_text.text)

# list_stuff = test_text.find_element_by_class_name("list list--check  ")
# for stuff in list_stuff:
#     lines = stuff.find_element_by_class_name("list__item")
#     print(lines.text)

# driver.close()   closes tab
driver.quit() # closes browser
