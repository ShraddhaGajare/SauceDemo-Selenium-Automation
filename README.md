# SauceDemo Selenium Automation Testing

A web automation testing project developed using **Python, Selenium WebDriver, Pytest, and Page Object Model (POM)**.

This project demonstrates automated functional testing of an e-commerce application, including login, shopping cart, and checkout workflows.

## Application Under Test

**Website:** https://www.saucedemo.com/

SauceDemo is a demo e-commerce website used for practicing software testing and automation.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Google Chrome
- pytest-html
- Git and GitHub
- GitHub Actions (CI/CD)

## Automated Test Scenarios

| Test Scenario | Description |
|---|---|
| Login UI Verification | Verify login fields are displayed |
| Valid Login | Verify login with valid credentials |
| Empty Password | Verify validation for an empty password |
| Add to Cart | Verify adding a product to the shopping cart |
| Remove from Cart | Verify removing a product from the cart |
| Complete Checkout | Verify the end-to-end checkout workflow |
| POM Login | Verify login using Page Object Model |
| POM Add to Cart | Verify cart functionality using POM |
| POM Remove from Cart | Verify product removal using POM |
| POM Checkout | Verify checkout using POM |

## Project Structure

```text
saucedemo-automation/
│
├── .github/
│   └── workflows/
│       └── selenium-tests.yml
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── conftest.py
├── test_pom_login.py
├── test_pom_cart.py
├── test_pom_remove_cart.py
├── test_pom_checkout.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Tests

**1. Clone the repository**

```bash
git clone https://github.com/ShraddhaGajare/SauceDemo-Selenium-Automation.git
```

**2. Navigate to the project directory**

```bash
cd SauceDemo-Selenium-Automation
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Run the POM test suite**

```bash
python -m pytest test_pom_login.py test_pom_cart.py test_pom_checkout.py -v -s
```

**5. Generate an HTML test report**

```bash
python -m pytest test_pom_login.py test_pom_cart.py test_pom_checkout.py -v -s --html=report.html --self-contained-html
```

## Test Reporting

The framework supports:

- HTML reports using pytest-html.
- Automatic screenshot capture when a test fails.
- Screenshot attachments in HTML reports.
- Combined reports for multiple test cases.

Generated reports and screenshots are excluded from Git tracking.

## Continuous Integration Using GitHub Actions

This project uses **GitHub Actions** to execute Selenium tests automatically whenever changes are pushed to the `main` branch.

The workflow:

1. Checks out the GitHub repository.
2. Sets up Python.
3. Installs dependencies.
4. Runs Selenium tests using headless Chrome.
5. Generates an HTML report.
6. Uploads the report as a downloadable artifact.

**Latest verified CI execution:** 3 passed, 0 failed.

## Key Learning Outcomes

- Designing automated test cases for web applications.
- Working with Selenium WebDriver and browser elements.
- Organizing automation using Page Object Model.
- Using Pytest fixtures for browser setup and teardown.
- Capturing screenshots for failed tests.
- Generating HTML test reports.
- Implementing CI using GitHub Actions.

## Project Purpose

This project was developed as a practical learning and portfolio project to demonstrate foundational Software QA and Test Automation skills.