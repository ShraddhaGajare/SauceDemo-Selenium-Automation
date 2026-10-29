
import os
import base64
import pytest

from selenium import webdriver
from pytest_html import extras


@pytest.fixture
def driver(request):

    print("\nOpening Chrome browser...")

    browser = webdriver.Chrome()
    browser.maximize_window()

    try:
        yield browser

    finally:
        # Get the test execution result
        report = getattr(request.node, "rep_call", None)

        # Capture screenshot only if the test failed
        if report and report.failed:

            os.makedirs("screenshots", exist_ok=True)

            test_name = request.node.name
            screenshot_path = f"screenshots/{test_name}.png"

            # Capture screenshot as bytes
            screenshot_bytes = browser.get_screenshot_as_png()

            # Save screenshot as a PNG file
            with open(screenshot_path, "wb") as file:
                file.write(screenshot_bytes)

            print(f"\nScreenshot saved: {screenshot_path}")

            # Convert screenshot bytes to Base64 text
            screenshot_base64 = base64.b64encode(
                screenshot_bytes
            ).decode("utf-8")

            # Attach screenshot to the HTML report
            if hasattr(report, "extras"):
                report.extras.append(
                    extras.png(screenshot_base64)
                )
            else:
                report.extras = [
                    extras.png(screenshot_base64)
                ]

            print("Screenshot attached to HTML report")

        input("\nPress Enter to close Chrome...")
        browser.quit()

        print("Chrome browser closed")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)
