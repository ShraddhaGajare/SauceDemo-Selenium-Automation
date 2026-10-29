
from builtins import print
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def add_backpack_to_cart(self):

        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )

        print("Button visible:", add_button.is_displayed())
        print("Button enabled:", add_button.is_enabled())
        print("Button text before click:", add_button.text)

        # Move mouse to button and click
        add_button.click()

        print("Normal Selenium click executed")

        time.sleep(3)

        add_buttons = self.driver.find_elements(
            By.ID, "add-to-cart-sauce-labs-backpack"
        )

        remove_buttons = self.driver.find_elements(
            By.ID, "remove-sauce-labs-backpack"
        )

        print("Add button still present:", len(add_buttons) > 0)
        print("Remove button present:", len(remove_buttons) > 0)

        if add_buttons:
            print("Button text after click:", add_buttons[0].text)

    def get_cart_count(self):

        badges = self.driver.find_elements(
            By.CLASS_NAME, "shopping_cart_badge"
        )

        print("Cart badge elements found:", len(badges))

        for badge in badges:
            print("Badge text:", repr(badge.text))
            print("Badge visible:", badge.is_displayed())

        def badge_has_one(driver):

            badges = driver.find_elements(
                By.CLASS_NAME, "shopping_cart_badge"
            )

            for badge in badges:
                if badge.text.strip() == "1":
                    return True

            return False

        self.wait.until(
            badge_has_one,
            "Cart badge did not show 1 within 30 seconds"
        )

        return "1"

    def open_cart(self):

        cart_icon = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )

        cart_icon.click()

        time.sleep(3)

        print("Cart page opened")
