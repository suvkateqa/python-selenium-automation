from selenium.webdriver.common.by import By
from behave import given, when, then
import ast


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
PRODUCT_PRICE = (By.CSS_SELECTOR, '#apex_desktop_qualifiedBuybox .a-price.reinventPricePriceToPayMargin.priceToPay span.a-offscreen')
COLOR_OPTIONS_TOP = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR_TOP = (By.CSS_SELECTOR, '#variation_color_name .selection')
COLOR_OPTIONS_JEANS = (By.CSS_SELECTOR, '#variation_color_name li') #same locator as TOP
CURRENT_COLOR_JEANS = (By.CSS_SELECTOR, '#variation_color_name .selection') #same locator as TOP



@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@when('Store product name and price')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')
    context.product_price = context.driver.find_element(*PRODUCT_PRICE).text
    print(f'Current product price: {context.product_price}')


# @then('Verify user can click through colors')
# def verify_user_can_select_colors(context):
#     context.driver.find_element(*COLOR_OPTIONS).click()  #click on one element
#
#     all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
#     print('All color options: ', all_color_options)
#     expected_colors = ['Army Green','Black', 'Brown', 'Burgundy', 'Caramel']
#
#
#     actual_colors = []
#     for color in all_color_options[:5]:
#         color.click()
#         current_color = context.driver.find_element(*CURRENT_COLOR).text
#         print('Current color: ', current_color)
#         actual_colors += [current_color]
#
#     assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'

# #Code when you need to re-use steps but when element locators are diffrent
# # Dictionary for color options and current color locators
# LOCATORS = {
#     "COLOR_OPTIONS_TOP": (By.CSS_SELECTOR, '#variation_color_name li'),
#     "CURRENT_COLOR_TOP": (By.CSS_SELECTOR, '#variation_color_name .selection'),
#     "COLOR_OPTIONS_JEANS": (By.CSS_SELECTOR, '#variation_color_name li'),
#     "CURRENT_COLOR_JEANS": (By.CSS_SELECTOR, '#variation_color_name .selection')
#     # Add more as needed
# }

@then('Verify user can click through colors and expects {expected_colors} with locator {locator}')
def verify_user_can_select_colors(context, expected_colors, locator):
    # Parse the expected_colors string to a Python list
    expected_colors = ast.literal_eval(expected_colors)

    # # Get the color options locator based on the provided locator key
    # color_options_locator = LOCATORS[locator]

    # Get all color options elements
    all_color_options = context.driver.find_elements(*COLOR_OPTIONS_TOP)
    print('All color options: ', all_color_options)

    actual_colors = []
    for color in all_color_options[:4]:
        # Click each color option
        color.click()
        # Get the current color text
        current_color = context.driver.find_element(*CURRENT_COLOR_TOP).text
        print('Current color: ', current_color)
        # Append the current color text to the actual_colors list
        actual_colors += [current_color]

    # Assert that the expected colors match the actual colors
    assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'