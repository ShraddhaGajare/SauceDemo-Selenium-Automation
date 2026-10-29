
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_add_to_cart_using_pom(driver):

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

    # STEP 2: Create ProductsPage object
    products_page = ProductsPage(driver)

    # STEP 3: Add Backpack to cart
    products_page.add_backpack_to_cart()

    # STEP 4: Verify cart badge
    cart_count = products_page.get_cart_count()

    assert cart_count == "1"

    print("Cart badge verified:", cart_count)

    # STEP 5: Open cart
    products_page.open_cart()

    # STEP 6: Verify product in cart
    product_name = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    assert product_name.text == "Sauce Labs Backpack"

    print("Product verified:", product_name.text)

    print("TEST PASSED: Add to cart using Page Object Model")
