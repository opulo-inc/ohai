# Planned Ship Date Formula Documentation

## Overview

This formula adjusts `Shipping Due dates` found in column `P` to ensure they are rounded back to the nearest Friday. If a date falls on a Thursday, it is moved to the next Friday. Dates on other days are adjusted to the previous Friday.

### Formula

```excel
=ARRAYFORMULA(IF(
  ISBLANK(A2:A), "", 
  IF(
    WEEKDAY(P2:P, 1) = 5, 
    P2:P + 1, 
    P2:P - MOD(WEEKDAY(P2:P, 1) + 1, 7)
  )
))
```

### Components

1. `ARRAYFORMULA(...)`:
    * Applies the formula to each cell in the range `P2:P`.

2. `IF(ISBLANK(A2:A), "", ...)`:
    * Checks if cells in column `A` are blank. If a cell is blank, it returns an empty string (`""`).

3. `WEEKDAY(P2:P, 1)`:
    * Returns the day of the week for each date in `P2:P` where:
        * 1 = Sunday
        * 2 = Monday
        * 3 = Tuesday
        * 4 = Wednesday
        * 5 = Thursday
        * 6 = Friday
        * 7 = Saturday

4. `IF(WEEKDAY(P2:P, 1) = 5, P2:P + 1, ...)`:
    * If the weekday is Thursday (5), it moves the date to the next Friday by adding 1 day.

5. `P2:P - MOD(WEEKDAY(P2:P, 1) + 1, 7)`:
    * `WEEKDAY(P2:P, 1) + 1`: Shifts the weekday values to align with a 0-based index.
    * `P2:P - MOD(..., 7)`: Subtracts the result from the date to adjust it to the previous Friday.

---

### Understanding `MOD`

The `MOD` function calculates the remainder after division. It is used to ensure that numbers wrap around a specified range, which is useful for dealing with circular sequences like days of the week.

#### Syntax

```excel
MOD(number, divisor)
```

* `number`: The value you want to divide.
* `divisor`: The value by which you want to divide.

#### In Use

* `MOD(10, 3)` results in `1` because 10 divided by 3 is 3 with a remainder of 1.
* `MOD(7, 7)` results in `0` because 7 divided by 7 is exactly 1 with no remainder.

#### In Our Formula

* `WEEKDAY(P2:P, 1) + 1` shifts the weekday values by 1, so Monday (2) becomes 3, and Friday (6) becomes 7.
* `MOD(..., 7)` ensures that values wrap around within the range of 0 to 6. This makes it possible to handle the circular nature of days in a week:
  * For Monday (2), `MOD(3, 7)` is 3.
  * For Friday (6), `MOD(7, 7)` is 0.

---

### Example Calculations

* Input Date: Wednesday, October 9
  * `WEEKDAY(P2, 1)`: `4` (Wednesday)
  * `WEEKDAY(P2, 1) + 1`: `5`
  * `MOD(5, 7)`: `5`
  * Result: Subtract 5 days from October 9, resulting in Friday, October 4

* Input Date: Thursday, October 10
  * `WEEKDAY(P2, 1)`: `5` (Thursday)
  * Condition: Since it is Thursday, the formula adds 1 day, resulting in Friday, October 11

## Summary

* `ARRAYFORMULA(...)` applies the formula to a range of cells.
* `IF(ISBLANK(P2:P), "", ...)` handles blank cells by returning an empty string.
* `WEEKDAY(P2:P, 1)` returns the day of the week as a number.
* `IF(WEEKDAY(P2:P, 1) = 5, P2:P + 1, ...)` moves Thursday dates to the next Friday.
* `MOD(WEEKDAY(P2:P, 1) + 1, 7)` calculates the number of days to subtract to round back to the previous Friday.
