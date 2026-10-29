
import os
import base64
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytest_html import extras


@pytest.fixture
def driver(request):

    print("\nOpening Chrome browser...")

    # Check whether the test is running on GitHub Actions
    is_ci = os.getenv("GITHUB_ACTIONS") == "true"

    chrome_options = Options()

    if is_ci:
        # Run Chrome without a visible window
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")

        print("Running Chrome in headless CI mode")

    browser = webdriver.Chrome(options=chrome_options)

    if not is_ci:
        browser.maximize_window()

    try:
        yield browser

    finally:
        report = getattr(request.node, "rep_call", None)

        if report and report.failed:

            os.makedirs("screenshots", exist_ok=True)

            test_name = request.node.name
            screenshot_path = f"screenshots/{test_name}.png"

            screenshot_bytes = browser.get_screenshot_as_png()

            with open(screenshot_path, "wb") as file:
                file.write(screenshot_bytes)

            print(f"\nScreenshot saved: {screenshot_path}")

            screenshot_base64 = base64.b64encode(
                screenshot_bytes
            ).decode("utf-8")

            if hasattr(report, "extras"):
                report.extras.append(
                    extras.png(screenshot_base64)
                )
            else:
                report.extras = [
                    extras.png(screenshot_base64)
                ]

            print("Screenshot attached to HTML report")

        # Pause only when running on your own computer
        if not is_ci:
            input("\nPress Enter to close Chrome...")

        browser.quit()

        print("Chrome browser closed")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)
