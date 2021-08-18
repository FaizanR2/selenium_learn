from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://en.wikipedia.org/wiki/DevOps")
link = driver.find_element_by_link_text("Main page")
link.click()

try:
     element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.LINK_TEXT, "The arts"))
     )
     element.click()

     driver.back() # goes back to the previous page
     # driver.forward() # goes to the forward page
except:
     driver.quit()