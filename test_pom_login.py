
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_login_using_pom(driver):

    # Create an object of LoginPage
    login_page = LoginPage(driver)

    # Open the website
    login_page.open_login_page()

    # Perform login
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Verify successful login
    wait = WebDriverWait(driver, 15)

    products_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    assert products_title.text == "Products"

    print("TEST PASSED: Login using Page Object Model")
