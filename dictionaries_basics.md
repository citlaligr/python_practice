
# 🧠 Exercise: Understanding Dictionaries

## 📝 Problem
Create a dictionary named car with the following keys: make, model, year, and color. Assign appropriate values to each key.
	"make": "Toyota",
	"model": "Camry",
	"year": 2020,
	"color": "Blue"

Print the value associated with the model key.
Add a new key called owner and assign it the name "Rahul".
Print the entire dictionary.


## Expected Output 
First fruit: apple
Last fruit: elderberry
Fruits from index 1 to 2: ['banana', 'cherry']

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

