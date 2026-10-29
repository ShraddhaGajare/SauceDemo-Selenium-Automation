
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_product_name(self):

        product = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        return product.text

    def remove_backpack(self):

        remove_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "remove-sauce-labs-backpack")
            )
        )

        remove_button.click()
        time.sleep(3)

        print("Backpack Remove button clicked")

    def is_cart_empty(self):

        self.wait.until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

        products = self.driver.find_elements(
            By.CLASS_NAME, "cart_item"
        )

        return len(products) == 0
