# Creating classes for the objects on the websites

from selenium.webdriver.common.by import By

class MainPageLocator(object):
    GO_BUTTON = (By.ID, "submit") # the name of button is 'GO' on the website, submit is the ID, By.ID is the access method


class SearchPageLocators(object):
    pass