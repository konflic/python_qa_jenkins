import allure

from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductPage(BasePage):
    """Страница продукта"""

    ADD_TO_WISHLIST = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    ADD_TO_CART = (By.CSS_SELECTOR, '#button-cart')

    @property
    def name(self):
        return None

    @allure.step("Adding product to wish list")
    def add_to_wishlist(self):
        self._click(self.ADD_TO_WISHLIST)
        return self

    @allure.step("Adding product to cart")
    def add_to_cart(self):
        self._click(self.ADD_TO_CART)
        return self
