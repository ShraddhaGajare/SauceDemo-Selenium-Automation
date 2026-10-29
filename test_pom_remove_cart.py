
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_remove_from_cart_using_pom(driver):

    # STEP 1: Login
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 15)

    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    print("Login successful")

    # STEP 2: Add Backpack
    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()

    # STEP 3: Verify cart badge
    assert products_page.get_cart_count() == "1"
    print("Cart badge verified: 1")

    # STEP 4: Open cart
    products_page.open_cart()

    # STEP 5: Verify Backpack
    cart_page = CartPage(driver)

    product_name = cart_page.get_product_name()

    assert product_name == "Sauce Labs Backpack"
    print("Product verified:", product_name)

    # STEP 6: Remove Backpack
    cart_page.remove_backpack()

    # STEP 7: Verify empty cart
    assert cart_page.is_cart_empty()

    # STEP 8: Verify cart badge disappeared
    wait.until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    print("Cart is empty and badge disappeared")
    print("TEST PASSED: Remove from cart using POM")
