
import time
import pytest

from selenium.webdriver.common.by import By


@pytest.mark.parametrize(
    "username,password,expected_result",
    [
        ("standard_user", "secret_sauce", "success"),
        ("invalid_user", "wrong_password", "error"),
        ("", "secret_sauce", "error"),
        ("standard_user", "", "error"),
    ]
)
def test_login_with_multiple_data(driver, username, password, expected_result):

    # Step 1: Open SauceDemo
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Step 2: Enter username
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys(username)
    time.sleep(1)

    # Step 3: Enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    time.sleep(1)

    # Step 4: Click Login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)

    # Step 5: Verify expected result
    if expected_result == "success":

        assert "inventory.html" in driver.current_url
        print("TEST PASSED: Valid login successful")

    else:

        error_message = driver.find_element(
            By.CSS_SELECTOR,
            '[data-test="error"]'
        )

        assert error_message.is_displayed()
        print("TEST PASSED: Invalid login correctly rejected")
