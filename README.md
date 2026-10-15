# SauceDemo Login Tests (Python + Pytest + Playwright)

End-to-end tests for the login flow of the public demo shop https://www.saucedemo.com.

## Covered scenarios
- Successful login with a valid user
- Locked-out user sees an error message
- Wrong password shows an error message
- Adding an item updates the cart badge
- Cart page lists the added item
- Removing an item empties the cart
- Complete checkout flow ends with the order confirmation
- Checkout form validates the required first name

## Setup
```
python -m venv .venv
# Windows: .venv\Scripts\activate    Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Run
```
pytest            # headless
pytest --headed   # watch the browser
```

## HTML report
```
pytest --html=report.html --self-contained-html
```
Open `report.html` in a browser. Failed tests get a screenshot when you add `--screenshot only-on-failure`.

## Continuous integration
Tests run automatically on every push and pull request via GitHub Actions
(`.github/workflows/tests.yml`). The HTML report is attached to each run as the `test-report` artifact.
