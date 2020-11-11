from selenium.common.exceptions import NoSuchElementException, TimeoutException


class element:

    def __init__(self, selector, index=0):
        self.selector = selector
        self.index = index

    def __call__(self, driver):
        try:
            return driver.find_elements(*self.selector)[self.index]
        except (IndexError, NoSuchElementException, TimeoutException):
            return False


class elements:

    def __init__(self, selector):
        self.selector = selector

    def __call__(self, driver):
        try:
            return driver.find_elements(*self.selector)
        except (IndexError, NoSuchElementException, TimeoutException):
            return False


class clickable:

    def __init__(self, element):
        self.element = element

    def __call__(self, driver):
        return self.element.is_enabled() and self.element.is_displayed()
