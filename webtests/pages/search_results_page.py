from selenium.webdriver.common.by import By
from webtests.pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    SUBNAV = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")

    def get_subnav_locator(self, category):
        pass


    def verify_search_result(self, expected_text):
       self.verify_text(expected_text, *self.SEARCH_RESULT)


    def verify_selected_department(self, category):
        locator =  self.get_subnav_locator(category)

        self.wait_for_element_appear(*self.locator)