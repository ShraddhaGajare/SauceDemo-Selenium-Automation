
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_using_pom(driver):

    # STEP 1: Login
    login_page = LoginPage(driver)

    login_page.open_login_page()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    wait = WebDriverWait(driver, 15)

    products_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    assert products_title.text == "Products"

    print("Login successful")

    # STEP 2: Add Backpack to cart
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()

    # STEP 3: Verify cart badge
    assert products_page.get_cart_count() == "1"

    print("Cart badge verified: 1")

    # STEP 4: Open cart
    products_page.open_cart()

    # STEP 5: Verify product in cart
    cart_page = CartPage(driver)

    product_name = cart_page.get_product_name()

    assert product_name == "Sauce Labs Backpack"

    print("Product verified in cart:", product_name)

    # STEP 6: Checkout
    checkout_page = CheckoutPage(driver)

    checkout_page.click_checkout()

    # STEP 7: Enter customer details
    checkout_page.enter_customer_details(
        "Test",
        "User",
        "400001"
    )

    # STEP 8: Continue to overview
    checkout_page.click_continue()

    # STEP 9: Verify product in summary
    summary_product = checkout_page.get_summary_product_name()

    assert summary_product == "Sauce Labs Backpack"

    print("Order summary verified:", summary_product)

    # STEP 10: Finish checkout
    checkout_page.click_finish()

    # STEP 11: Verify confirmation
    confirmation_message = checkout_page.get_confirmation_message()

    assert confirmation_message == "Thank you for your order!"

    print("Order confirmation:", confirmation_message)

    print("TEST PASSED: Complete checkout using POM")
