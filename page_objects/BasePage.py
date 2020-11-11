import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from helpers.waits import element, clickable, elements
from .common.Alert import Alert
from .common.Search import Search
from .common.TopMenu import TopMenu


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.alert = Alert(self.driver)
        self.search = Search(self.driver)
        self.top_menu = TopMenu(self.driver)

    @allure.step("Getting element {selector}[{index}]")
    def _element(self, selector, index: int = 0, all=False):
        if type(selector) == str:
            selector = (By.LINK_TEXT, selector)
        try:
            if all:
                return WebDriverWait(self.driver, 3).until(elements(selector))
            return WebDriverWait(self.driver, 3).until(element(selector, index))
        except TimeoutException:
            raise AssertionError(f"Element {selector} was not found on page")

    @allure.step("Clicking element {selector}[{index}]")
    def _click(self, selector, index: int = 0):
        element = self._element(selector, index)
        try:
            WebDriverWait(self.driver, 3).until(clickable(element))
            element.click()
        except Exception as e:
            raise AssertionError(f"Something was wrong! {e}")

    @allure.step("Input {value} into {selector}[{index}]")
    def _input(self, selector, value, index=0):
        element = self._element(selector, index)
        try:
            element.clear()
            element.send_keys(value)
        except Exception as e:
            raise AssertionError(f"Something was wrong! {e}")

    @allure.step("Waiting for element {selector}[{index}] to be visible")
    def _wait_for_visible(self, selector, index=0, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self._element(selector, index)))

    def _get_element_text(self, selector, index):
        return self._element(selector, index).text
