
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_checkout(self):

        checkout_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        )

        checkout_button.click()
        time.sleep(2)

        print("Checkout page opened")

    def enter_customer_details(self, first_name, last_name, postal_code):

        first_name_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )

        first_name_field.send_keys(first_name)
        time.sleep(2)

        last_name_field = self.driver.find_element(
            By.ID, "last-name"
        )

        last_name_field.send_keys(last_name)
        time.sleep(2)

        postal_code_field = self.driver.find_element(
            By.ID, "postal-code"
        )

        postal_code_field.send_keys(postal_code)
        time.sleep(2)

        print("Customer details entered")

    def click_continue(self):

        continue_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        )

        continue_button.click()
        time.sleep(2)

        print("Checkout overview opened")

    def get_summary_product_name(self):

        product = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        return product.text

    def click_finish(self):

        finish_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "finish")
            )
        )

        finish_button.click()
        time.sleep(3)

        print("Finish button clicked")

    def get_confirmation_message(self):

        confirmation = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        return confirmation.text
