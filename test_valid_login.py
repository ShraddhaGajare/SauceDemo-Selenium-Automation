
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login():

    driver = webdriver.Chrome()

    try:
        # Open the SauceDemo website
        driver.get("https://www.saucedemo.com/")

        wait = WebDriverWait(driver, 15)

        # Find the username field
        username = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )

        # Enter the demo username
        username.send_keys("standard_user")

        # Find and enter the demo password
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        # Find and click the Login button
        login_button = driver.find_element(
            By.ID, "login-button"
        )
        login_button.click()

        # Wait until the Products page appears
        products_title = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        # Verify the expected page title
        assert products_title.text == "Products"

        print("TEST PASSED: Valid login successful")
        print("Current URL:", driver.current_url)

    finally:
        driver.quit()
