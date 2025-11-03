from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OffPlanPage(BasePage):
    OFF_PLAN_BUTTON = (By.CSS_SELECTOR, '[wized="newOffPlanLink"]')
    #OFF_PLAN_BUTTON = (By.XPATH, "//div[@class='g-menu-text' and normalize-space()='Off-plan']")

    FILTER_DROPDOWN = (By.CSS_SELECTOR, '[data-test-id="search-and-filters-button"]')
    PRESALE_OPTION = (By.CSS_SELECTOR, '[data-test-id="filter-badge-presale"]')
    PRODUCT_ITEMS = (By.CSS_SELECTOR, '[data-test-id^="project-card-"]')
    SALE_STATUS = (By.XPATH, "//span[@data-test-id='project-card-sale-status' and normalize-space()='Presale']")


    def open_off_plan(self):
        self.click(*self.OFF_PLAN_BUTTON)

    def filter_by_presale(self):
        self.click(*self.FILTER_DROPDOWN)

        # Wait for dropdown to open (headless-safe)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.PRESALE_OPTION)
            )
        except Exception:
            # If not visible yet, click dropdown again
            self.driver.execute_script("arguments[0].click();",
                                       self.driver.find_element(*self.FILTER_DROPDOWN))
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.PRESALE_OPTION)
            )

        # Click on Presale option (headless-safe)
        self.click(*self.PRESALE_OPTION)

    def verify_presale_results(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(self.SALE_STATUS)
        )

        status_elements = self.get_elements(*self.SALE_STATUS)
        assert len(status_elements) > 0, "No sale status elements found after filtering."

        for el in status_elements:
            status = el.text.strip().lower()
            assert "presale" in status, f"Found non-Presale product: {status}"
