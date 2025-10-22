from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, '[id="email-2"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-name="Password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '.login-button.w-button')


    def login(self, username, password):
        self.type_text(*self.USERNAME, text=username)
        self.type_text(*self.PASSWORD, text=password)
        self.click(*self.LOGIN_BTN)
