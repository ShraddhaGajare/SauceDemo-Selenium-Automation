
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_page_with_shared_fixture(driver):

    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)

    wait = WebDriverWait(driver, 15)

    # Find username field
    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )

    # Find password field
    password = driver.find_element(
        By.ID, "password"
    )

    # Verify both fields are visible
    assert username.is_displayed()
    assert password.is_displayed()

    print("TEST PASSED: Shared fixture works successfully")
