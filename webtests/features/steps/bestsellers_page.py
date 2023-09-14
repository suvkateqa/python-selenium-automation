from selenium.webdriver.common.by import By
from behave import given, when, then


BESTSELLERS_TOP_BAR = (By.CSS_SELECTOR, "#zg_header a")
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

#Use this code when verifying elements that refresh the page to avoid Stale exception error

@then('User can click through top links and verify correct page opens')
def click_through_top_links(context):
    top_links = context.driver.find_elements(*BESTSELLERS_TOP_BAR) #[WebEl1, WebElem2, WebElem3..]
    print(top_links)

    for i in range(len(top_links)): #for x from 0-4, it takes a number of links in top_links which is 5 links
        link_to_click = context.driver.find_elements(*BESTSELLERS_TOP_BAR)[i]
        link_text = link_to_click.text
        print(link_text)

        link_to_click.click()

        header_text = context.driver.find_element(*HEADER).text
        print(header_text)
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'


