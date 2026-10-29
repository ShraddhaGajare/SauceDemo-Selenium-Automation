
import pytest
from selenium import webdriver


@pytest.fixture
def driver():

    print("\nOpening Chrome browser...")

    browser = webdriver.Chrome()
    browser.maximize_window()

    try:
        # Provide Chrome to the test
        yield browser

    finally:
        # Allow time to inspect the browser
        input("\nPress Enter to close Chrome...")

        # Close Chrome after the test
        browser.quit()

        print("Chrome browser closed")
