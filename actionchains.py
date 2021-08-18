from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # allows us to use common keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10) # waiting for 5 seconds before all of the elements get loaded in

big_cookie = driver.find_element_by_id("bigCookie")
no_of_cookies = driver.find_element_by_id("cookies")
# gets all element that have productPrice
# the string concatenation allows i to act as productPrice0 or productPrice1
# the range in the loop sets the integar, in this case we go from 0 to 1 and back to 0
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

action = ActionChains(driver)
action.click(big_cookie) # clicks wherever the cursor is,however, we gave the argument to the big cookie here
for i in range(500): # a loop for performing the click action 500 times
    action.perform()  # actually executes all of the actions
    count = int(no_of_cookies.text.split(" ")[0]) # the split function only extracts the NUMBER from the no_of_cookies.text
                                                # we then typecast that NUMBER value to integar
    for item in items: # the loop for upgrading an item whenever we have enough cookies
        value = int(item.text)
        if value <= count: # checks if we hav enough for an upgrade
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item) # moves the cursor to the upgrade button
            upgrade_action.click()
            upgrade_action.perform()
