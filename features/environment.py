from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from app.application import Application



def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


#------------------------------------------------------------------------
#headless mode
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--window-size=1920,1080")
    #chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--remote-debugging-pipe")  # <-- enforces true headless
    #chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #chrome_options.add_experimental_option('useAutomationExtension', False)



    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(service=service, options=chrome_options)
    #context.driver.implicitly_wait(4)

#------------------------------------------------------------------------
   # using FireFox
    #service = FirefoxService(GeckoDriverManager().install())
    #context.driver = webdriver.Firefox(service=service)

    #Window setup and waits
    #context.driver.set_window_size(1920, 1080)
    #context.driver.implicitly_wait(4)
    #context.driver.maximize_window()
#-----------------------------------------------------------------------
def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
