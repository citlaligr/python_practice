## 📝 Problem
Create variables to store personal information, including age, height, and favorite color.

## Requirements
- `age`: integer value (e.g., 25)
- `height`: float value (e.g., 5.9)
- `favorite_color`: string value (e.g., "blue")

Display each variable along with its data type using the `type()` function.

## Expected Output
Age: 25 | Type: <class 'int'>
Height: 5.9 | Type: <class 'float'>
Favorite Color: blue | Type: <class 'str'>

## Source
Exercise inspired by a Python course on Udemy.
	
## 💻 Solution
```python

age=17
height=4.5
favorite_color="yellow"

print(f"Age: {age} | Type:{type(age)}")
print(f"Height: {height} | Type:{type(height)}")
print("Favorite Color: {favorite_color} | Type:{type(favorite_color)} ")
