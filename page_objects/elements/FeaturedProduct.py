from selenium.webdriver.common.by import By


class FeaturedProduct:
    NAME = (By.CSS_SELECTOR, '.caption h4 a')
    TO_COMPARISON = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    TO_WISH_LIST = (By.CSS_SELECTOR, '[data-original-title="Compare this Product"]')
    TO_CART = (By.XPATH, '//*[text()="Add to Cart"]')

    def __init__(self, element):
        self.element = element

    @property
    def name(self):
        return self.element.find_element(*self.NAME).text

    def add_to_wish_list(self):
        self.element.find_element(*self.TO_WISH_LIST).click()

    def add_to_comparison(self):
        self.element.find_element(*self.TO_COMPARISON).click()

    def add_to_cart(self):
        self.element.find_element(*self.TO_CART).click()
