from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULT = (By.CSS_SELECTOR, "[data-component-type='s-search-results']")
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')



@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(2)


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    context.app.search_results_page.verify_search_result(expected_result)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULT)
    # In Selenium method product.find_element finds an element inside another element  [WebElement1,WebElement2, WebElement3,.. ]
    print(f'Amount of products found: {len(all_products)}')
    print(all_products)

    for product in all_products:
        print(product)
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Product image is missing'
        product_title = product.find_element(*PRODUCT_TITLE).text
        assert product_title, 'Product title is missing'


@then('Verify {categoty} department is selected')
def verify_selected_department(context, category):
    context.app.search_results_page.verify_selected_department(category)
