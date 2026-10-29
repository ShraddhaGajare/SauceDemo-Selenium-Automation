
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_add_to_cart():

    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        # STEP 1: Open SauceDemo
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        wait = WebDriverWait(driver, 15)

        # STEP 2: Enter username
        username = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )
        username.send_keys("standard_user")
        time.sleep(2)

        # STEP 3: Enter password
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        time.sleep(2)

        # STEP 4: Click Login
        driver.find_element(
            By.ID, "login-button"
        ).click()

        # STEP 5: Verify Products page
        products_title = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        assert products_title.text == "Products"

        print("Login successful")
        time.sleep(3)

        # STEP 6: Find Add to cart button
        add_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )

        print("Add button found")

        # STEP 7: Click Add to cart
        add_button.click()
        print("Clicked Add to cart")
        time.sleep(3)

        # STEP 8: Check whether button changed to Remove
        remove_buttons = driver.find_elements(
            By.ID, "remove-sauce-labs-backpack"
        )

        print("Remove button found:", len(remove_buttons) > 0)

        # STEP 9: Check cart badge
        try:
            cart_badge = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "shopping_cart_badge")
                )
            )

            print("Cart badge:", cart_badge.text)

            assert cart_badge.text == "1"

        except TimeoutException:
            print("ERROR: Cart badge did not appear")

            badges = driver.find_elements(
                By.CLASS_NAME, "shopping_cart_badge"
            )

            print("Number of cart badges found:", len(badges))
            print("Current URL:", driver.current_url)

            raise AssertionError(
                "Cart badge was not visible after adding product"
            )

        # STEP 10: Open shopping cart
        cart_link = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )
        cart_link.click()
        time.sleep(3)

        # STEP 11: Verify product
        product_name = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        print("Product in cart:", product_name.text)

        assert product_name.text == "Sauce Labs Backpack"

        print("TEST PASSED: Add to cart successful")

    finally:
        # Pause even if the test fails
        input("Inspect Chrome, then press Enter to close...")

        driver.quit()
