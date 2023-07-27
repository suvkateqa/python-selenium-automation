from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')

    def input_search_text(self, input_value):
        self.input_text(input_value, *self.AMAZON_SEARCH_INPUT_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)
