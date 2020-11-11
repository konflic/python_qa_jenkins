import allure

from page_objects import MainPage, UserPage, ProductPage, CartPage


@allure.feature("Wish List")
@allure.title("Add product to wish list from product page")
def test_add_to_product_to_wish_list(browser):
    product_name = MainPage(browser).get_featured_product_name(1)
    MainPage(browser) \
        .click_featured_product(1) \
        .add_to_wishlist() \
        .alert.click_login()
    UserPage(browser) \
        .login_user() \
        .open_wishlist() \
        .verify_product(product_name)


@allure.feature("Cart")
@allure.title("Add product to cart from product page")
def test_add_product_to_cart(browser):
    product_name = MainPage(browser).get_featured_product_name(1)
    MainPage(browser).click_featured_product(1)
    ProductPage(browser) \
        .add_to_cart() \
        .alert.click_to_cart()
    CartPage(browser) \
        .verify_product(product_name) \
        .checkout()
    UserPage(browser) \
        .login_user() \
        .verify_payment_form()


@allure.feature("Wish List")
@allure.title("Add product to wish list from main page")
def test_add_product_to_wish_list_from_main_page(browser):
    product_name = MainPage(browser).get_featured_product_name(1)
    MainPage(browser) \
        .add_featured_product_to_cart(1) \
        .alert.click_to_cart()
    CartPage(browser) \
        .verify_product(product_name) \
        .checkout()
    UserPage(browser) \
        .login_user() \
        .verify_payment_form()
