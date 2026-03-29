
# 🧠 Exercise: Working with Dictionaries

## 📝 Problem
Practice using dictionaries to store and manipulate structured data.

## Requirements
- Create a dictionary named `car` with the following keys:
  - `make`
  - `model`
  - `year`
  - `color`

- Assign appropriate values to each key.
- Access and display the value associated with the `model` key.
- Add a new key `owner` with a string value.
- Print the complete dictionary.

## Expected Output
Camry  
{'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'color': 'Blue', 'owner': 'Rahul'}

## Concepts Practiced
- Dictionaries
- Key-value pairs
- Accessing values
- Updating dictionaries

## Source
Exercise inspired by a Python course on Udemy.

---

## 💻 Solution
```python
car={
    "make":"Toyota",
    "model":"Camry",
    "year":2020,
    "color":"Blue"
    }

print (f"Car model: {car['model']}")

car["owner"]="Rahul"

print (f"Updated car dictionary: {car}")

