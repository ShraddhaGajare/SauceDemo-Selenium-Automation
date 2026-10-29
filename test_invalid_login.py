
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_username_password():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 15)

        # Enter incorrect demo credentials
        username = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )
        username.send_keys("invalid_user")

        password = driver.find_element(By.ID, "password")
        password.send_keys("wrong_password")

        # Click Login
        driver.find_element(By.ID, "login-button").click()

        # Wait for the error message
        error_message = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )

        print("Actual error:", error_message.text)

        # Verify the error message
        assert "Username and password do not match" in error_message.text

        print("TEST PASSED: Invalid login rejected")

    finally:
        driver.quit()


def test_empty_username_password():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 15)

        # Click Login without entering credentials
        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "login-button")
            )
        )
        login_button.click()

        # Check required-field error
        error_message = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )

        print("Actual error:", error_message.text)

        assert "Username is required" in error_message.text

        print("TEST PASSED: Empty username rejected")

    finally:
        driver.quit()


def test_empty_password():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 15)

        # Enter username only
        username = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )
        username.send_keys("standard_user")

        # Leave password empty and click Login
        driver.find_element(By.ID, "login-button").click()

        error_message = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )

        print("Actual error:", error_message.text)

        assert "Password is required" in error_message.text

        print("TEST PASSED: Empty password rejected")

    finally:
        driver.quit()
