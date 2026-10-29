# SauceDemo Selenium Automation Testing

![Selenium Tests](https://github.com/ShraddhaGajare/SauceDemo-Selenium-Automation/actions/workflows/selenium-tests.yml/badge.svg)

An automated web application testing project developed using **Python, Selenium WebDriver, Pytest, and Page Object Model (POM)**.

This project demonstrates functional UI testing, data-driven testing, end-to-end checkout automation, HTML reporting, and CI/CD integration using GitHub Actions.

## Application Under Test

**Website:** https://www.saucedemo.com/

SauceDemo is a demo e-commerce application used for practicing software testing and automation.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Google Chrome (Headless and Visible Mode)
- Pytest HTML Reporting
- Git and GitHub
- GitHub Actions (CI/CD)

## Automated Test Scenarios

| Test Case | Description |
|---|---|
| POM Login | Verify successful login using valid credentials |
| Add to Cart | Add Sauce Labs Backpack and verify the cart |
| Remove from Cart | Remove a product and verify the cart is empty |
| Complete Checkout | Verify the end-to-end checkout workflow and order confirmation |
| Data-Driven Login 1 | Verify successful login with valid credentials |
| Data-Driven Login 2 | Verify error handling for invalid username and password |
| Data-Driven Login 3 | Verify validation when username is empty |
| Data-Driven Login 4 | Verify validation when password is empty |

**Total automated tests: 8**

## Project Structure

```text
saucedemo-automation/
|
+-- .github/
|   +-- workflows/
|       +-- selenium-tests.yml
|
+-- pages/
|   +-- login_page.py
|   +-- products_page.py
|   +-- cart_page.py
|   +-- checkout_page.py
|
+-- conftest.py
+-- test_pom_login.py
+-- test_pom_cart.py
+-- test_pom_remove_cart.py
+-- test_pom_checkout.py
+-- test_data_driven_login.py
+-- requirements.txt
+-- .gitignore
+-- README.md
```

## How to Run the Tests

### 1. Clone the Repository

```bash
git clone https://github.com/ShraddhaGajare/SauceDemo-Selenium-Automation.git
```

### 2. Navigate to the Project

```bash
cd SauceDemo-Selenium-Automation
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run All 8 Automated Tests

```bash
python -m pytest test_pom_login.py test_pom_cart.py test_pom_remove_cart.py test_pom_checkout.py test_data_driven_login.py -v -s
```

### 5. Generate an HTML Test Report

```bash
python -m pytest test_pom_login.py test_pom_cart.py test_pom_remove_cart.py test_pom_checkout.py test_data_driven_login.py -v -s --html=report.html --self-contained-html
```

## Framework Features

- Page Object Model for reusable page interactions.
- Pytest fixtures for browser setup and teardown.
- Explicit waits for handling dynamic web elements.
- Data-driven login testing using multiple input combinations.
- Headless Chrome execution for CI environments.
- Automatic screenshot capture on test failures.
- HTML reports using pytest-html.
- GitHub Actions for automated test execution.

## Continuous Integration Using GitHub Actions

The project includes a GitHub Actions workflow that executes Selenium automation tests when changes are pushed to the `main` branch.

The workflow:

1. Checks out the GitHub repository.
2. Configures Python.
3. Installs project dependencies.
4. Executes Selenium tests using headless Chrome.
5. Generates an HTML test report.
6. Uploads the report as a downloadable artifact.

**Verified GitHub Actions Execution**

| Metric | Result |
|---|---|
| Environment | Ubuntu Linux |
| Python Version | 3.12.15 |
| Test Framework | Pytest 9.2.0 |
| Browser | Headless Chrome |
| Total Tests | 8 |
| Passed | 8 |
| Failed | 0 |
| Execution Time | 33.51 seconds |

**GitHub Actions:** https://github.com/ShraddhaGajare/SauceDemo-Selenium-Automation/actions

## Test Reporting

The automation framework generates HTML reports using pytest-html.

When a test fails, the framework captures a browser screenshot and attaches it to the test report.

GitHub Actions uploads the generated HTML report as an artifact named `selenium-html-report`.

## Key Learning Outcomes

Through this project, I gained practical experience in:

- Writing and executing automated UI test cases.
- Implementing Selenium WebDriver using Python.
- Designing reusable Page Object Model classes.
- Creating data-driven tests with Pytest.
- Using explicit waits for web element synchronization.
- Validating shopping cart and checkout workflows.
- Capturing screenshots and generating HTML reports.
- Managing automation code using Git and GitHub.
- Configuring CI/CD test execution using GitHub Actions.
- Debugging Selenium tests in headless Chrome.

## Project Purpose

This project was developed as a hands-on QA automation learning and portfolio project to demonstrate practical skills in **Software Testing, Selenium Python Automation, Pytest, POM, and CI/CD**.