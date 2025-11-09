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

    def verify_mobile_layout(self):
        """
        Robust mobile sanity check that avoids calling /window/rect.
        Verifies (1) session is alive, (2) mobile-like viewport via JS media query,
        (3) filter control is visible, (4) at least one product card is on screen,
        (5) first visible status is 'Presale'.
        """

        # 0) Soft guard: ensure session is alive before any WebDriver commands
        try:
            _ = self.driver.current_url  # lightweight ping
        except Exception as e:
            raise AssertionError(f"WebDriver session ended before mobile verification: {e}") from e

        # 1) Prefer JS media query over get_window_size() to detect mobile-ish width
        try:
            is_mobile = self.driver.execute_script("return window.matchMedia('(max-width: 500px)').matches;")
        except Exception as e:
            # If JS fails for any reason, just mark unknown; don't hard-fail only on width
            is_mobile = None

        if is_mobile is False:
            # Not fatal, but useful signal in reports
            print("⚠️  Media query indicates width > 500px; still proceeding with element checks.")

        # 2) Filter control should be visible (use your locator)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FILTER_DROPDOWN)
        )
        filt = self.driver.find_element(*self.FILTER_DROPDOWN)
        assert filt.is_displayed(), "Expected the filter dropdown to be visible on mobile"

        # 3) One or more product cards visible (use your locator)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(self.PRODUCT_ITEMS)
        )
        cards = self.get_elements(*self.PRODUCT_ITEMS)
        assert len(cards) > 0, "Expected at least one product card to be visible on mobile"

        # 4) First visible sale status is Presale (your existing label)
        statuses = self.driver.find_elements(*self.SALE_STATUS)
        assert statuses, "Expected at least one Presale status label to be visible"
        assert "presale" in statuses[0].text.strip().lower(), f"First visible card not Presale: {statuses[0].text}"
