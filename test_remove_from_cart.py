
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_remove_from_cart():

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

        # STEP 6: Add Backpack to cart
        add_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )

        add_button.click()
        print("Clicked Add to cart")
        time.sleep(3)

        # STEP 7: Verify cart badge shows 1
        cart_badge = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        assert cart_badge.text == "1"
        print("Cart badge before removal:", cart_badge.text)
        time.sleep(2)

        # STEP 8: Click Remove
        remove_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "remove-sauce-labs-backpack")
            )
        )

        remove_button.click()
        print("Clicked Remove")
        time.sleep(3)

        # STEP 9: Verify cart badge disappears
        wait.until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        badges = driver.find_elements(
            By.CLASS_NAME, "shopping_cart_badge"
        )

        assert len(badges) == 0

        print("Cart badge disappeared")

        # STEP 10: Verify Add to cart button returns
        add_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )

        assert add_button.is_displayed()

        print("Add to cart button is visible again")
        print("TEST PASSED: Product removed successfully")

    finally:
        input("Inspect Chrome, then press Enter to close...")
        driver.quit()
