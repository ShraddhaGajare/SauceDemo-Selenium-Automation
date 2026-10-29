
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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

        print("Add button displayed:", add_button.is_displayed())
        print("Add button enabled:", add_button.is_enabled())

        add_button.click()

        print("Add button clicked")

        try:
            remove_button = self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, "remove-sauce-labs-backpack")
                )
            )

        except TimeoutException:
            print("ERROR: Remove button did not appear")
            print("Current URL:", self.driver.current_url)

            add_buttons = self.driver.find_elements(
                By.ID, "add-to-cart-sauce-labs-backpack"
            )

            print(
                "Add button still present:",
                len(add_buttons) > 0
            )

            badges = self.driver.find_elements(
                By.CLASS_NAME, "shopping_cart_badge"
            )

            print(
                "Cart badge:",
                badges[0].text if badges else "Not present"
            )

            raise

        assert remove_button.is_displayed(), (
            "Remove button is not visible"
        )

        print("Backpack successfully added to cart")

    def get_cart_count(self):

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

        cart_icon = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )

        print("URL before cart click:", self.driver.current_url)
        print("Cart icon displayed:", cart_icon.is_displayed())
        print("Cart icon enabled:", cart_icon.is_enabled())

        # JavaScript click experiment for headless Chrome
        self.driver.execute_script(
            "arguments[0].click();",
            cart_icon
        )

        print("Cart icon clicked")
        print("URL immediately after click:", self.driver.current_url)

        try:
            self.wait.until(
                EC.url_contains("/cart.html")
            )

        except TimeoutException:
            print("ERROR: Cart page did not open")
            print("Final URL:", self.driver.current_url)

            cart_titles = self.driver.find_elements(
                By.CLASS_NAME, "title"
            )

            if cart_titles:
                print(
                    "Current page title:",
                    cart_titles[0].text
                )

            raise

        cart_title = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        assert cart_title.text == "Your Cart", (
            "Cart page did not open correctly"
        )

        print("Cart page opened successfully")
        print("Current URL:", self.driver.current_url)
