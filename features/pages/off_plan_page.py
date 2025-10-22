from selenium.webdriver.common.by import By
from .base_page import BasePage

class OffPlanPage(BasePage):
    OFF_PLAN_BUTTON = (By.CSS_SELECTOR, '[wized="newOffPlanLink"]')
    FILTER_DROPDOWN = (By.CSS_SELECTOR, '[data-test-id="search-and-filters-button"]')
    PRESALE_OPTION = (By.CSS_SELECTOR, '[data-test-id="filter-badge-presale"]')
    PRODUCT_ITEMS = (By.CSS_SELECTOR, '[data-test-id^="project-card-"]')
    SALE_STATUS = (By.CSS_SELECTOR, '[data-test-id="project-card-sale-status"]')


    def open_off_plan(self):
        self.click(*self.OFF_PLAN_BUTTON)

    def filter_by_presale(self):
        self.click(*self.FILTER_DROPDOWN)
        self.click(*self.PRESALE_OPTION)

    def verify_presale_results(self):
        status_elements = self.get_elements(*self.SALE_STATUS)
        assert len(status_elements) > 0, "No sale status elements found after filtering."

        for el in status_elements:
            status = el.text.strip().lower()
            assert "presale" in status, f"Found non-Presale product: {status}"
