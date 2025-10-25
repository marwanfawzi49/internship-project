from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #def click(self, by, locator):
        #self.wait.until(EC.element_to_be_clickable((by, locator))).click()
    def click(self, by, locator):
        """Wait for element and click, with JS fallback (for headless stability)."""
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, locator)))
            element.click()
        except Exception:
            # fallback for headless or overlay issues
            element = self.driver.find_element(by, locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, by, locator, text):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        element.send_keys(text)

    def get_elements(self, by, locator):
        return self.wait.until(EC.presence_of_all_elements_located((by, locator)))
