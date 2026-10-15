# SauceDemo E2E Tests (Python + Pytest + Playwright)

[![Tests](https://github.com/biltekinhamza/saucedemo-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/biltekinhamza/saucedemo-tests/actions/workflows/tests.yml)

End-to-end tests for the login, cart and checkout flows of the public demo shop
https://www.saucedemo.com, plus two documented bug reports.

## Covered scenarios
| File | Scenario |
|---|---|
| `test_login.py` | Successful login with a valid user |
| `test_login.py` | Locked-out user sees an error message |
| `test_login.py` | Wrong password shows an error message |
| `test_cart_checkout.py` | Adding an item updates the cart badge |
| `test_cart_checkout.py` | Cart page lists the added item |
| `test_cart_checkout.py` | Removing an item empties the cart |
| `test_cart_checkout.py` | Complete checkout ends with the order confirmation |
| `test_cart_checkout.py` | Checkout form requires the first name |
| `test_known_bugs.py` | Two known `problem_user` defects, kept as expected-failure tests |

## Bug reports
- [BUG-001 – Checkout blocked: last name typed into first name](bug-reports/BUG-001-checkout-last-name-typed-into-first-name.md) (High)
- [BUG-002 – Every product shows the same image](bug-reports/BUG-002-all-product-images-identical.md) (Medium)

## Setup
```
python -m venv .venv
# Windows: .venv\Scripts\activate    Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Run
```
pytest            # headless
pytest --headed   # watch the browser
```

## HTML report
```
pytest --html=report.html --self-contained-html --screenshot only-on-failure
```
Open `report.html` in a browser. Failed tests get a screenshot.

## Continuous integration
Tests run automatically on every push and pull request via GitHub Actions
(`.github/workflows/tests.yml`). The HTML report is attached to each run as the `test-report` artifact.

## Project structure
- `conftest.py` – shared `logged_in_page` fixture (standard user already logged in)
- `test_login.py`, `test_cart_checkout.py`, `test_known_bugs.py` – tests
- `bug-reports/` – written bug reports with steps, expected and actual results
