# BUG-002: Every product shows the same placeholder image

| Field | Value |
|---|---|
| **Severity** | Medium (shop is usable but products cannot be told apart visually) |
| **Priority** | Medium |
| **Status** | Open |
| **Environment** | https://www.saucedemo.com, Chrome (Chromium, Playwright 1.6x), Windows 10 |
| **Test account** | `problem_user` / `secret_sauce` |
| **Reproducibility** | 100 % (3 of 3 attempts) |
| **Automated check** | `test_known_bugs.py::test_problem_user_sees_distinct_product_images` (marked `xfail`) |

## Summary
On the Products page, all 6 items load the same image file instead of their own product
picture.

## Steps to reproduce
1. Open https://www.saucedemo.com.
2. Log in with username `problem_user` and password `secret_sauce`.
3. Look at the product images on the Products page.

## Expected result
Each of the 6 products shows its own image (backpack, bike light, T-shirt, ...).

## Actual result
All 6 products use the same image source (`/assets/sl-404-....jpg`, a "404" placeholder),
so the products look identical.

## Impact
Customers cannot identify products from pictures, which hurts trust and conversion.

## Notes
- `standard_user` shows 6 different images.
