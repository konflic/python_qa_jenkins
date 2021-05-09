import allure


@allure.feature("Comparison")
@allure.title("Adding product to comparison")
def test_add_product_to_comparison(browser):
    allure.attach(name="screenshot", body=browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    raise AssertionError("This test fails!")
