# AI Code Review Assignment (Python)

## Candidate
- Name: Eyob Amare Tesfaye
- Approximate time spent: 25 mins

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- **Incorrect divisor**: The code divides the total amount by `len(orders)` (the total number of orders) instead of the count of *non-cancelled* orders. This makes the calculated average lower than it should be because it includes cancelled orders in the count but not the sum.
- **Division by Zero**: If the list `orders` is empty, `len(orders)` is 0, causing the program to crash with a `ZeroDivisionError`.

### Edge cases & risks
- **All orders cancelled**: If all orders are cancelled, the total is 0, but `count` is still positive. The result 0 is technically correct numerically (0/5 = 0), but semantically we might expect it to handle "no valid orders" differently or at least we need to be aware.
- **Missing keys**: If an order dictionary doesn't have a "status" or "amount" key, the code will crash.

### Code quality / design issues
- **Variable naming**: `count` is misleading because it's set to the total length at the start, not the count of items we act on.

## 2) Proposed Fixes / Improvements
### Summary of changes
- I changed the logic to only increment the counter (`count`) when we find a valid (non-cancelled) order.
- I added a check at the start to return 0 immediately if the list is empty.
- I added a check at the end to return 0 if `count` is 0 (e.g., if all orders were cancelled) to prevent division by zero.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- **Mixed statuses**: A list with both "completed" and "cancelled" orders to verify the math ignores the cancelled ones correctly.
- **Empty list**: To ensure it returns 0 instead of crashing.
- **Only cancelled orders**: To ensure it returns 0 and doesn't crash or return a weird number.
- **Missing data**: Input where an order is missing the "status" key to see if it needs safe access (like `.get()`).

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation claims it "correctly excludes cancelled orders from the calculation," but the code actually *included* them in the divisor (the count), making the calculation wrong. It was misleading.

### Rewritten explanation
- This function calculates the average dollar value of valid orders. It adds up the amounts from orders that aren't "cancelled" and divides that sum by the number of valid orders found. If there are no orders to average, it returns 0.

## 4) Final Judgment
- Decision: Reject
- Justification: The function produced mathematically incorrect results for any input containing cancelled orders, and it crashed on empty inputs. It needed significant logic corrections.
- Confidence & unknowns: High confidence. The math error is clear.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- **Weak validation**: The code only checks if an email has an "@" symbol. This means strings like "@" or "hello@" or " @ " are counted as valid emails, which is incorrect.

### Edge cases & risks
- **Non-string inputs**: If the list contains `None` or integers, the code will crash because you can't check for `"@"` in them.
- **Empty strings**: Pass the check (count as 0), but good to keep in mind.

### Code quality / design issues
- **Too simple**: Real-world email validation usually requires checking for a domain part (like `.com`) and a username part.

## 2) Proposed Fixes / Improvements
### Summary of changes
- I imported the `re` (regex) module to use a pattern matching check.
- I implemented a check `^[^@]+@[^@]+\.[^@]+$` which ensures there is text before the @, text after the @, a dot, and text after the dot.
- I added a type check `isinstance(email, str)` to valid crashing on bad data types.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- **Invalid formats**: Strings like "missing_at.com", "user@domain", "@domain.com", "user@.com" to ensure they are rejected.
- **Non-string types**: Passing `None` or a number `123` to correct handling.
- **Valid emails**: Standard emails like "name@example.com" to ensure they are accepted.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- It claimed to count "valid" emails, but its definition of valid (just contains "@") was too loose to be useful. It also didn't "safely ignore" non-string invalid entries; it would have crashed.

### Rewritten explanation
- This function counts how many items in a list are properly formatted email addresses. It uses a pattern check to ensure each email has a username, an "@" symbol, and a domain with a dot (like "user@example.com"). It also safely skips any data that isn't text.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The validation logic was insufficient for any real-use case. While not crashing on strings, it would accept garbage data as valid emails.
- Confidence & unknowns: High confidence.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- **Incorrect divisor**: Similar to Task 1, `count` is set to `len(values)` at the start. This means `None` values are included in the count, diluting the average (making it smaller than it should be).
- **Crash on non-numbers**: The code assumes everything that isn't `None` can be turned into a float. If the list has a string like "error", `float("error")` will crash the program.

### Edge cases & risks
- **Division by Zero**: If the list is empty (or has only `None`s), `count` might be 0 (if fixed) or `len` is 0, causing a crash.

### Code quality / design issues
- **Assumption of data quality**: It assumes too much about the input data (that it's all numbers or None).

## 2) Proposed Fixes / Improvements
### Summary of changes
- I moved the `count` increment inside the loop, so it only counts values we actually add to the total.
- I added a `try-except` block to catch `ValueError` and `TypeError`. This allows the loop to safely skip strings or other non-number data.
- I added a check for `count == 0` at the end to avoid division by zero.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- **Mixed Valid/Invalid**: A list like `[10, None, "bad", 20]`. Result should be 15 (Average of 10 and 20).
- **All None**: To ensure it returns 0.
- **Strings**: Inputs like `["10.5", "abc"]` to see if it parses the number string and skips the letters.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The original explanation was factually incorrect. It said it "safely handles mixed input types," but the code would crash on non-numeric strings. It also implied the average was accurate, which was false due to the divisor bug.

### Rewritten explanation
- This function finds the average of a series of measurements. It is smart enough to skip `None` values (missing data) and text that isn't a number. It calculates the average based only on the valid numbers it found.

## 4) Final Judgment
- Decision: Reject
- Justification: The function had critical logic errors (average calculation) and runtime errors (handling mixed types) that directly contradicted its stated purpose.
- Confidence & unknowns: High.


