
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_empty_password():

    # Open Chrome browser
    driver = webdriver.Chrome()

    try:
        # Maximize Chrome
        driver.maximize_window()

        # Open SauceDemo website
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        # Wait up to 15 seconds for elements
        wait = WebDriverWait(driver, 15)

        # Find username field
        username = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )

        # Enter valid username
        username.send_keys("standard_user")
        time.sleep(3)

        # Find password field
        password = driver.find_element(
            By.ID, "password"
        )

        # Verify password field is empty
        assert password.get_attribute("value") == ""

        print("Password field is empty")
        time.sleep(2)

        # Find Login button
        login_button = driver.find_element(
            By.ID, "login-button"
        )

        # Click Login
        login_button.click()
        time.sleep(3)

        # Find validation error message
        error_message = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )

        # Print actual error
        print("Actual Error:", error_message.text)

        # Verify expected error
        assert "Password is required" in error_message.text

        print("TEST PASSED: Empty password rejected")

        # Keep browser open to observe result
        input("Press Enter to close Chrome...")

    finally:
        # Close Chrome
        driver.quit()
