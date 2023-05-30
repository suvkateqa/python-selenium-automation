from selenium.webdriver.common.by import By
from behave import given, when, then


ISSUE_CARD_CONTAINER = (By.CSS_SELECTOR, '.issue-card-container')
ISSUE_CARD_CONTAINER_LINKS = (By.CSS_SELECTOR, '.issue-card-container .issue-card-wrapper')
SEARCH_OUR_HELP_LIBRARY_HEADER = (By.XPATH, "//h2[text()='Search our help library']")
SEARCH_OUR_HELP_LIBRARY_FIELD = (By.ID, 'hubHelpSearchInput')
ALL_HELP_TOPICS_HEADER = (By.XPATH, "//h2[text()='All help topics']")
RECOMMENDED_TOPICS_CONTAINER = (By.CSS_SELECTOR, '.help-topics-list-wrapper')
RECOMMENDED_TOPICS_CONTAINER_LINKS = (By.CSS_SELECTOR, '.help-topics-list-wrapper li')


@given('Open Customer Service page')
def open_customer_service_page(context):
    context.driver.get('https://www.amazon.com/hz/contact-us/foresight/hubgateway')


@then('Verify Issue card container present')
def verify_issue_card_container_present(context):
    # print('Find element')
    issue_container = context.driver.find_element(*ISSUE_CARD_CONTAINER)
    print(issue_container)


@then('Verify Search our help library header present')
def verify_search_our_help_library_header_present(context):
    search_our_help_library_header = context.driver.find_element(*SEARCH_OUR_HELP_LIBRARY_HEADER)
    print(search_our_help_library_header)

@then('Verify Search our help library field present')
def verify_search_our_help_library_field(context):
    search_our_help_library_field = context.driver.find_element(*SEARCH_OUR_HELP_LIBRARY_FIELD)
    print(search_our_help_library_field)


@then('Verify All help topics header present')
def verify_all_help_topics_header_present(context):
    all_help_topics_header = context.driver.find_element(*ALL_HELP_TOPICS_HEADER)
    print(all_help_topics_header)


@then('Verify Recommended topics container present')
def verify_recommended_topics_container_present(context):
    recommended_topics_container = context.driver.find_element(*RECOMMENDED_TOPICS_CONTAINER)
    print(recommended_topics_container)


@then('Verify Recommended Topics container has {expected_amount} links')
def recommended_topics_container_links_count(context, expected_amount):
    expected_amount = int(expected_amount)
    recommended_topics_container_links = context.driver.find_elements(*RECOMMENDED_TOPICS_CONTAINER_LINKS)
    print(recommended_topics_container_links)
    print('\nLink count: ', len(recommended_topics_container_links))
    assert len(recommended_topics_container_links) == expected_amount, f'Expected {expected_amount} links but got {len(recommended_topics_container_links)}'


@then('Verify Issue card container has {expected_amount} links')
def verify_issue_card_container(context, expected_amount):
    expected_amount = int(expected_amount)
    issue_card_container_links = context.driver.find_elements(*ISSUE_CARD_CONTAINER_LINKS)
    print('\nLink count: ', len(issue_card_container_links))
    assert len(issue_card_container_links) == expected_amount, f'Expected {expected_amount} links but got {len(issue_card_container_links)}'





