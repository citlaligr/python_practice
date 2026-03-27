
# 🧠 Exercise: Working with Lists

## 📝 Problem
Create a list named fruits that contains below five different fruit names (strings).
- "apple", "banana", "cherry", "date", "elderberry"

Print the first and last elements of the list.

Use slicing to print the second and third fruits from the list.

## Expected Output 
First fruit: apple
Last fruit: elderberry
Fruits from index 1 to 2: ['banana', 'cherry']

---

## 💻 Solution
```python
fruits=["apple","banana","cherry","date","elderberry"]
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
sli=slice(1, 3)
print(f"Fruits from index 1 to 2: {fruits[sli]}") 

