# features/app/application.py
from ..pages.login_page import LoginPage
from ..pages.off_plan_page import OffPlanPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.off_plan_page = OffPlanPage(driver)
