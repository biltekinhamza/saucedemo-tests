# BUG-001: Checkout is blocked – text typed in "Last Name" goes into "First Name"

| Field | Value |
|---|---|
| **Severity** | High (user cannot complete a purchase) |
| **Priority** | High |
| **Status** | Open |
| **Environment** | https://www.saucedemo.com, Chrome (Chromium, Playwright 1.6x), Windows 10 |
| **Test account** | `problem_user` / `secret_sauce` |
| **Reproducibility** | 100 % (3 of 3 attempts) |
| **Automated check** | `test_known_bugs.py::test_problem_user_can_enter_last_name` (marked `xfail`) |

## Summary
When logged in as `problem_user`, typing into the **Last Name** field on the checkout
information page writes the text into the **First Name** field instead. The Last Name
field stays empty, so the form shows "Last Name is required" and the order cannot be placed.

## Steps to reproduce
1. Open https://www.saucedemo.com.
2. Log in with username `problem_user` and password `secret_sauce`.
3. Click **Add to cart** on "Sauce Labs Backpack".
4. Click the cart icon, then click **Checkout**.
5. Type `Ali` in **First Name**.
6. Type `Yilmaz` in **Last Name**.
7. Type `34000` in **Zip/Postal Code**.
8. Click **Continue**.

## Expected result
- First Name contains `Ali`, Last Name contains `Yilmaz`.
- The user moves on to the "Checkout: Overview" page (`/checkout-step-two.html`).

## Actual result
- First Name contains `Yilmaz` (the first value is overwritten), Last Name is empty.
- The page stays on `/checkout-step-one.html` and shows the error
  **"Error: Last Name is required"**.

## Impact
A `problem_user` customer can never finish checkout, even when every field is filled in
correctly. Every order from that account is lost.

## Notes
- `standard_user` does not have this problem (see `test_complete_checkout`).
- Workaround: none found from the user side.
