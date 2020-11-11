import allure

from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CartPage(BasePage):
    """Экран корзины"""

    BUTTONS = (By.CSS_SELECTOR, '.buttons')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, BUTTONS[1] + ' a.btn-primary')

    @allure.step("Clicking checkout button")
    def checkout(self):
        self._click(self.CHECKOUT_BUTTON)

    @allure.step("Verify that product {name} link is visible")
    def verify_product(self, name):
        self._wait_for_visible(name)
        return self
