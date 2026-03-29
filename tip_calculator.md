# Tip Calculator Exercise

## Problem
Create a program that calculates the total tip and splits the bill among a group of people. The program should handle user inputs for bill amount, tip percentage, and number of people, and return the amount each person should pay.

## Requirements
- Total bill amount
- Tip percentage (suggested: 10, 12, 15)
- Number of people to split the bill

## Concepts Practiced
- Variables and data types (`float`, `int`)
- Arithmetic operations (`+`, `*`, `/`)
- Type conversion (`float()`, `int()`)
- Conditional statements (`if/else`)
- Rounding numbers (`round()`)
- String formatting (`f-strings`)

## Source
Exercise inspired by a Python course on Udemy.

## Code
```python
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

if people <= 0:
    print("Number of people must be greater than 0.")
else:
    per_person = total_bill / people
    final_amount = round(per_person, 2)
    print(f"Each person should pay: ${final_amount:.2f}")