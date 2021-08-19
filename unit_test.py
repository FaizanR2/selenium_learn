import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    # Initializing stage, will run everytime test cases are run

    def setUp(self):
        print("Setup")
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.python.org/")

    # Test cases phase, functions starting with the word 'test' will run automatically due to unittest

    def test_search_python(self):
        mainPage = page.MainPage(self.driver) # storing the mainpage class from page file
        assert mainPage.is_title_matches() # assert tests if a condition is true, if false, it stops the program with error
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

    # End or clean up phase

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
