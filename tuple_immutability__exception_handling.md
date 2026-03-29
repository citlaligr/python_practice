## 📝 Problem
Work with a tuple to store basic personal information and explore its immutability.

## Requirements
- Create a tuple named `person` with the following values:
  - Name (string)
  - Age (integer)
  - Height (float)

- Display the second element of the tuple.
- Attempt to modify the name stored in the tuple.
- Handle the resulting error using a try-except block.

## Expected Behavior
- The program should print the second element (age).
- An error should occur when trying to modify the tuple, demonstrating that tuples are immutable.

## Concepts Practiced
- Tuples
- Immutability
- Exception Handling (try-except)

## Source
Exercise inspired by a Python course on Udemy.

## 💻 Solution 

person=("Rahul", 25, 5.9)
print(f"Age: {person[1]}")
try:
    person[0] = "John"
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")
