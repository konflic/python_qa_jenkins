import allure

from helpers.test_data import create_random_user
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class UserPage(BasePage):
    """Страница пользователя"""

    RIGHT_MENU = (By.CSS_SELECTOR, '#column-right')
    WISH_LIST = (By.CSS_SELECTOR, RIGHT_MENU[1] + ' a:nth-child(5)')
    PAYMENT_FORM = (By.CSS_SELECTOR, '#payment-new')
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[value=Login]')

    @allure.step("Login into user account")
    def login_user(self, email=None, password="test"):
        if email is None:
            email = create_random_user(self.driver.db)
        self._input(self.LOGIN_EMAIL_INPUT, email)
        self._input(self.LOGIN_PASSWORD_INPUT, password)
        self._click(self.LOGIN_BUTTON)
        return self

    @allure.step("Opening user wishlist")
    def open_wishlist(self):
        self._click(self.WISH_LIST)
        return self

    @allure.step("Checking that payment form present")
    def verify_payment_form(self):
        self._wait_for_visible(self.PAYMENT_FORM)
        return self

    @allure.step("Verifying that product {name} link is visible")
    def verify_product(self, name):
        self._wait_for_visible(name)
        return self
