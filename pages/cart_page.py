
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

        # Wait until Remove button is clickable
        remove_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "remove-sauce-labs-backpack")
            )
        )

        # Click Remove
        remove_button.click()

        # Wait until the Backpack disappears from cart
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

        print("Backpack successfully removed from cart")

    def is_cart_empty(self):

        # Wait until no cart item is visible
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "cart_item")
            )
        )

        # Check whether any cart items remain
        products = self.driver.find_elements(
            By.CLASS_NAME, "cart_item"
        )

        return len(products) == 0
