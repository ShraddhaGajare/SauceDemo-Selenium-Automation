
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# FIXTURE: Opens and closes Chrome
@pytest.fixture
def driver():

    print("Opening Chrome browser")

    browser = webdriver.Chrome()
    browser.maximize_window()

    # Give browser to the test function
    yield browser

    # Cleanup after test
    input("Inspect Chrome, then press Enter to close...")

    browser.quit()
    print("Chrome browser closed")


# TEST CASE 1: Verify login page
def test_login_page(driver):

    driver.get("https://www.saucedemo.com/")
    time.sleep(3)

    wait = WebDriverWait(driver, 15)

    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )

    password = driver.find_element(By.ID, "password")

    assert username.is_displayed()
    assert password.is_displayed()

    print("TEST PASSED: Login page fields visible")


# TEST CASE 2: Verify successful login
def test_valid_login(driver):

    driver.get("https://www.saucedemo.com/")
    time.sleep(3)

    wait = WebDriverWait(driver, 15)

    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )
    username.send_keys("standard_user")
    time.sleep(2)

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    time.sleep(2)

    driver.find_element(By.ID, "login-button").click()

    products_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    assert products_title.text == "Products"

    print("TEST PASSED: Valid login successful")
