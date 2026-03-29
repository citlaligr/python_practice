
# 🧠 Exercise: List Access and Slicing

## 📝 Problem
Practice working with lists by accessing elements and extracting subsets using slicing.

## Requirements
- Create a list named `fruits` containing multiple string values.
- Access and display the first and last elements of the list.
- Use slicing to extract and display a subset of elements (specifically the second and third items).

## Expected Behavior
- The program should print:
  - The first element
  - The last element
  - A sublist containing the second and third elements

## Concepts Practiced
- Lists
- Indexing
- Negative indexing
- List slicing

## Source
Exercise inspired by a Python course on Udemy.

---

## 💻 Solution
```python
fruits=["apple","banana","cherry","date","elderberry"]
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
sli=slice(1, 3)
print(f"Fruits from index 1 to 2: {fruits[sli]}") 

