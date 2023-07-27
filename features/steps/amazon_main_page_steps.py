from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# AMAZON_SEARCH_INPUT_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td.navFooterDescItem')
HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop a.nav-a[data-csa-c-type='link']")
BESTSELLER_LINKS = (By.CSS_SELECTOR, '#zg_header li')
SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-signin-button')

@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@given('Open BestSellers page')
def open_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@when('Input text {search_word}')
def input_search_word(context, search_word):
    # context.driver.find_element(*AMAZON_SEARCH_INPUT_FIELD).send_keys(search_word)
    context.app.header.input_search_text(search_word)


@when('Click on search button')
def click_search(context):
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.header.click_search()


@when('Click Sign In from popup')
def click_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN)).click()
    # can add an error message, for example:
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN),
        message='Sign in button not clickable'
    ).click()


@when('Wait for {sec} seconds')
def wait_for_sec(context, sec):
    #In Behave everything is string. '8' -> 8 with int
    sleep(int(sec))


@then('Verify Sign in popup shown')
def verify_signin_popup_visiable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN),
        message='Signin btn not clickable'
    )


@then('Verify Sign in popup disappears')
def verify_signin_popup_not_visiable(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(SIGN_IN_BTN),
        message='Signin btn did not disappear'
    )


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    print('Find element')
    element = context.driver.find_element(*HAM_MENU)
    # print(element)


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    # print('Original Type: ', type(expected_amount)) #'36'
    expected_amount = int(expected_amount)
    # print('Type after converting: ', type(expected_amount)) # => 36
    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    # print(footer_links)
    # print('\nLink count: ',len(footer_links))
    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links but got {len(footer_links)}'


@then('Verify that header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links but got {len(header_links)}'


@then('Verify that Bestsellers page has {expected_amount} links')
def verify_bestseller_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    bestseller_links = context.driver.find_elements(*BESTSELLER_LINKS)
    # print(bestseller_links)
    print('\nLink count: ',len(bestseller_links))
    assert len(bestseller_links) == expected_amount, f'Expected {expected_amount} links but got {len(bestseller_links)}'



