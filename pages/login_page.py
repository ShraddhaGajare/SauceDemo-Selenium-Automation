
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_login_page(self):
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(3)

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )

        username_field.send_keys(username)
        time.sleep(2)

    def enter_password(self, password):
        password_field = self.driver.find_element(
            By.ID, "password"
        )

        password_field.send_keys(password)
        time.sleep(2)

    def click_login(self):
        login_button = self.driver.find_element(
            By.ID, "login-button"
        )

        login_button.click()
        time.sleep(3)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
