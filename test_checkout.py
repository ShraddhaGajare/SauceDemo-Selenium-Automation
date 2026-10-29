
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_complete_checkout():

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
        password = driver.find_element(
            By.ID, "password"
        )
        password.send_keys("secret_sauce")
        time.sleep(2)

        # STEP 4: Click Login
        driver.find_element(
            By.ID, "login-button"
        ).click()

        products_title = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        assert products_title.text == "Products"
        print("Login successful")
        time.sleep(3)

        # STEP 5: Add Backpack to cart
        add_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )
        add_button.click()

        cart_badge = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )
        assert cart_badge.text == "1"

        print("Backpack added to cart")
        time.sleep(3)

        # STEP 6: Open cart
        driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()

        product = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )
        assert product.text == "Sauce Labs Backpack"

        print("Product verified in cart")
        time.sleep(3)

        # STEP 7: Click Checkout
        checkout_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        )
        checkout_button.click()
        time.sleep(3)

        # STEP 8: Enter customer details
        first_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )
        first_name.send_keys("Test")
        time.sleep(2)

        last_name = driver.find_element(
            By.ID, "last-name"
        )
        last_name.send_keys("User")
        time.sleep(2)

        postal_code = driver.find_element(
            By.ID, "postal-code"
        )
        postal_code.send_keys("400001")
        time.sleep(2)

        print("Customer details entered")

        # STEP 9: Continue checkout
        driver.find_element(
            By.ID, "continue"
        ).click()
        time.sleep(3)

        # STEP 10: Verify order summary
        summary_product = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        assert summary_product.text == "Sauce Labs Backpack"

        print("Order summary verified")
        time.sleep(3)

        # STEP 11: Complete checkout
        finish_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "finish")
            )
        )
        finish_button.click()
        time.sleep(3)

        # STEP 12: Verify confirmation
        confirmation = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        assert confirmation.text == "Thank you for your order!"

        print("Order confirmation:", confirmation.text)
        print("TEST PASSED: Complete checkout successful")

    finally:
        input("Inspect Chrome, then press Enter to close...")
        driver.quit()
