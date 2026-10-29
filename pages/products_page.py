
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def add_backpack_to_cart(self):

        # Find the Add to Cart button
        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )

        # Click Add to Cart
        add_button.click()

        # Verify button changes to Remove
        remove_button = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "remove-sauce-labs-backpack")
            )
        )

        assert remove_button.is_displayed(), (
            "Remove button is not visible"
        )

        print("Backpack successfully added to cart")

    def get_cart_count(self):

        # Wait until cart badge displays 1
        badge = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "shopping_cart_badge"),
                "1"
            )
        )

        print("Cart badge verified:", badge.text)

        return badge.text.strip()

    def open_cart(self):

        # Wait until cart icon is clickable
        cart_icon = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )

        # Open shopping cart
        cart_icon.click()

        # Wait until cart page opens
        self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        print("Cart page opened")
