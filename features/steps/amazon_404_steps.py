from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


DOG_IMG = (By.CSS_SELECTOR, 'img#d')

@given('Store original window')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)

@when('Click on a dog image')
def click_img(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles #collect those window IDs ['1A35CF60B92F1E54303AE3C5B97A6ACC', 'AC5630FAB6BA6A76857590C170C0B933']
    print('\nALL WINDOWS: ', windows)
    context.driver.switch_to.window(windows[1]) #we call the new window with index [1] AC5630FAB6BA6A76857590C170C0B933

    context.current_window = context.driver.current_window_handle
    print('\nAFTER WE SWITCHED: ')
    print(context.current_window)


@then('Verify blog is opened')
def verify_blog_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/'))


@then('Close blog')
def close_blog(context):
    context.driver.close()


@then('Return to the original window')
def switch_to_original_window(context):
    context.driver.switch_to(context.original_window)





