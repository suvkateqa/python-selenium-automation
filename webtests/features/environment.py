from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webtests.app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # service = Service('/Users/ekaterinasuvorova/Automation2023/Kate_github_project/webtests/chromedriver')
    service = Service('/Users/ekaterinasuvorova/Automation2023/Kate_github_project/geckodriver')
    # context.driver = webdriver.Chrome(service=service)
    context.driver = webdriver.Firefox(service=service)
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 4)
    context.app = Application(driver=context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
