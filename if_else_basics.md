
# 🧠 Exercise: Conditional Logic with If-Else Statements

## 📝 Problem
Practice using conditional statements to control program behavior based on variable values.

## Requirements
- Create a variable `greeting` and assign it a string value.
- Use an `if-else` statement to evaluate the value of the variable:
  - If the value is `"Hello"`, display a personalized greeting message.
  - Otherwise, display a generic greeting.
- After the conditional block, print a message indicating the program has finished execution.

## Expected Output

If greeting is "Hello":
Hello there!  
How can I assist you today?  
Program has completed.

If greeting is not "Hello":
Greetings!  
Program has completed.

## Concepts Practiced
- Conditional statements (`if/else`)
- String comparison
- Control flow
- Print statements

## Source
Exercise inspired by a Python course on Udemy.

---

## 💻 Solution
```python
greeting ="Hello" #To test else: greeting="Hi"
if greeting =="Hello":
    print("Hello there!")
    print("How can I assist you today?")
else:
    print("Greetings!")
print("Program has completed.")
