"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/10/2020
Homework Problem: #5.15.5
Description:

---

**5.15.5: Write a python program that does the following:**

The formula for calculating the amount of money in a savings account that begins with an initial principal value (P) and earns annual interest (i) for (n) years is: P(1 + i)n Note that i is a decimal, not a percent interest rate: .1 NOT 10%

* Prompt the user on three lines for principal, percent interest rate and number of years to invest (using descriptive prompts)
    * Use a while loop to keep prompting until entries are valid

* Call your function calc_compound_interest() that:
    * takes the arguments principle, int_rate, years
    * uses the above formula to calculate the ending value of the account
    * returns the value

* Call a second function calc_compound_interest_recursive() that:
    * takes the arguments principle, int_rate, years
    * calculates the value **recursively** (calling a base calculation over and over instead of using the number of year as an exponent.)
    * return that value

* Print both values with clear descriptions and formatted with thousand commas and 2 decimal places. Then print whether the two values are equal when rounded to 4 decimal places.


"""