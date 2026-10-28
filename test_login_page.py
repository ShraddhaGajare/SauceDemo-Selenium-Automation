from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_page_elements():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 15)

        username = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )

        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        assert username.is_displayed()
        assert password.is_displayed()
        assert login_button.is_displayed()

        print("TEST PASSED: Login page elements are visible")

    finally:
        driver.quit()
