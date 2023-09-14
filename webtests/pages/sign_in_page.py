from selenium.webdriver.common.by import By
from webtests.pages.base_page import Page


class SigninPage(Page):
    SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_FIELD = (By.ID, 'ap_email')


    def verify_sign_in_opened(self):
        self.verify_url_contains_query('https://www.amazon.com/ap/signin')