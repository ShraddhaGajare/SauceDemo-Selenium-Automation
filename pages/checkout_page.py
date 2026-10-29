
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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

        print("URL before checkout:", self.driver.current_url)
        print("Checkout displayed:", checkout_button.is_displayed())
        print("Checkout enabled:", checkout_button.is_enabled())

        # JavaScript click experiment for headless Chrome
        self.driver.execute_script(
            "arguments[0].click();",
            checkout_button
        )

        print("Checkout button clicked")
        print("URL after click:", self.driver.current_url)

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, "first-name")
                )
            )

        except TimeoutException:
            print("ERROR: Checkout information page did not open")
            print("Current URL:", self.driver.current_url)

            checkout_buttons = self.driver.find_elements(
                By.ID, "checkout"
            )

            print(
                "Checkout button still present:",
                len(checkout_buttons) > 0
            )

            raise

        print("Checkout page opened")

    def enter_customer_details(self, first_name, last_name, postal_code):

        first_name_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )

        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(
            By.ID, "last-name"
        )
        last_name_field.send_keys(last_name)

        postal_code_field = self.driver.find_element(
            By.ID, "postal-code"
        )
        postal_code_field.send_keys(postal_code)

        print("Customer details entered")

    def click_continue(self):

        continue_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        )

        continue_button.click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "finish")
            )
        )

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

        self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        print("Finish button clicked")

    def get_confirmation_message(self):

        confirmation = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        return confirmation.text

