# Playwright Test Automation

Automated tests for the SauceDemo web app (UI) and the JSONPlaceholder API, built with Python, Playwright and pytest.

## What is tested

- Login: valid and invalid credentials
- Shopping cart: adding a product and opening the cart
- Checkout: moving through the checkout steps
- API: GET, POST, DELETE and a negative test (404), including a parametrized test

## How to run

Install the dependencies:

    pip install pytest-playwright requests
    playwright install

Run all tests:

    pytest