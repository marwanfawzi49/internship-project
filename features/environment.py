from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from app.application import Application
import os



def browser_init(context):
   #___________________________________________________________________
    # Browser Stack 
    username = os.getenv("BROWSERSTACK_USERNAME")
    access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

    options = webdriver.ChromeOptions()
    options.browser_version = "latest"
    options.platform_name = "OS X Sonoma"

    
    bstack_options = {
        "os": "OS X",
        "osVersion": "Sonoma",
        "projectName": "Soft.reelly Presale Filter",
        "buildName": "BrowserStack Internship Build",
        "sessionName": "Presale filter scenario",
        "local": "false"
    }
    options.set_capability("bstack:options", bstack_options)

    context.driver = webdriver.Remote(
        command_executor=f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )
# ------------------------------------------------------------------------
# 🟡 LOCAL CHROME (for reference, disabled)
# Uncomment to run locally with Chrome instead of BrowserStack
#

# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# 🟡 HEADLESS MODE (optional local headless config)
#
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--window-size=1920,1080")
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--remote-debugging-pipe")  # enforce true headless
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     chrome_options.add_experimental_option('useAutomationExtension', False)
#
#     service = Service(ChromeDriverManager().install())
#     context.driver = webdriver.Chrome(service=service, options=chrome_options)
#     context.driver.implicitly_wait(4)
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# 🟡 FIREFOX (optional)
#
#     service = FirefoxService(GeckoDriverManager().install())
#     context.driver = webdriver.Firefox(service=service)
#
#     context.driver.set_window_size(1920, 1080)
#     context.driver.implicitly_wait(4)
#     context.driver.maximize_window()
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
def before_scenario(context, scenario):
    print('\nStarted scenario:', scenario.name)
    browser_init(context)  


def before_step(context, step):
    print('\nStarted step:', step.name)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed:', step.name)


def after_scenario(context, scenario):
    context.driver.quit()
