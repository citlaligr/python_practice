# 🧠 Exercise: Working with Lists

## 📝 Problem
Create three variables: age, height, and favorite_color. Assign them values 25, 5.9, blue:
	- age: an integer (e.g., 25)
	- height: a float (e.g., 5.9)
	- favorite_color: a string (e.g., "blue")
	
Use the print function to display each variable and its type using the type() function.

## Expected Output 

Age: 25 | Type: <class 'int'>
Height: 5.9 | Type: <class 'float'>
Favorite Color: blue | Type: <class 'str'>
	
## 💻 Solution
```python

age=25
height=5.9
favorite_color="blue"

print(f"Age: {age} | Type:{type(age)}")
print(f"Height: {height} | Type:{type(height)}")
print("Favorite Color: {favorite_color} | Type:{type(favorite_color)} ")
