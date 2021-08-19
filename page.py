from locator import *
from element import BasePageElement

# Class for locating each element
class SearchTextElement(BasePageElement):
    locator = "q" # the name= of the search bar on python website

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


# Creating a class for each page of the website we are testing

class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocator.GO_BUTTON) # the * seperates or opens the elements
        element.click()

class SearchResultPage(BasePage):

    def is_result_found(self):
        return "No Results Found" not in self.driver.page_source