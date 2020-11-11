from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from helpers.waits import element, clickable


class Alert:
    SUCCESS_ALERT = (By.CSS_SELECTOR, '.alert-success')
    LOGIN = (By.LINK_TEXT, "login")
    TO_CART = (By.LINK_TEXT, "shopping cart")

    def __init__(self, driver):
        self.driver = driver

    @property
    def success_alert(self):
        return WebDriverWait(self.driver, 3).until(element(self.SUCCESS_ALERT))

    def click_login(self):
        # А как нам заиспоьзовать здесь BasePage?
        self.success_alert.find_element(*self.LOGIN).click()

    def click_to_cart(self):
        self.success_alert.find_element(*self.TO_CART).click()
