from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_search_result(self, expected_text):
        actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
        assert expected_text == actual_result, f'Expected {expected_text} but got actual {actual_result}'
