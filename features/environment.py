from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(chrome_options=options)

    # context.driver = webdriver.Chrome(executable_path='/Users/inna/Documents/GitHub/chromedriver')
    # context.browser = webdriver.Safari()
    # context.driver = webdriver.Firefox(executable_path='/Users/inna/Documents/GitHub/geckodriver')

    ### Headless Mode ###
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    context.driver = webdriver.Chrome(executable_path='/Users/inna/Documents/GitHub/chromedriver',chrome_options=options)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


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
