import allure
import time

from selenium.webdriver.common.by import By
from .BasePage import BasePage
from .ProductPage import ProductPage
from page_objects.elements import FeaturedProduct


class MainPage(BasePage):
    """Главная страница"""

    IT = (By.CSS_SELECTOR, "#content > div.row")
    FPRODUCTS = (By.CSS_SELECTOR, IT[1] + ' .product-layout')

    @property
    def _featured_products(self):
        return self._element(self.FPRODUCTS, all=True)

    @allure.step("Clicking fetured product number: {number}")
    def click_featured_product(self, number):
        self._featured_products[number - 1].click()
        return ProductPage(self.driver)

    @allure.step("Getting featured product {number} name")
    def get_featured_product_name(self, number):
        return FeaturedProduct(self._featured_products[number - 1]).name

    @allure.step("Clicking Add to Cart on featured product {number}")
    def add_featured_product_to_cart(self, number):
        FeaturedProduct(self._featured_products[number - 1]).add_to_cart()
        return self

    @allure.step("Clicking Add to Comparison on featured product {number}")
    def add_featured_product_to_comparison(self, number):
        FeaturedProduct(self._featured_products[number - 1]).add_to_comparison()
        return self

    @allure.step("Clicking Add to Wish List on featured product {number}")
    def add_featured_product_to_wish_list(self, number):
        FeaturedProduct(self._featured_products[number - 1]).add_to_wish_list()
        return self
