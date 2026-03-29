# 🧠 Exercise: Time-Based Conditional Greetings

## 📝 Problem
Use conditional logic to display different messages based on a numeric value representing time.

## Requirements
- Create a variable (e.g., `hour`) and assign it a numeric value.
- Use `if-elif-else` statements to evaluate the value and display:
  - "Good Morning" for values between 5 and 11
  - "Good Afternoon" for values between 12 and 17
  - "Good Evening" for values between 18 and 21
  - "Good Night" for all other values
- Print a final message indicating the program has completed.

## Expected Output

For input 10:
Good Morning  
Greeting code has completed.

For input 15:
Good Afternoon  
Greeting code has completed.

## Concepts Practiced
- Conditional statements (`if/elif/else`)
- Range evaluation
- Control flow
- Logical conditions

## Source
Exercise inspired by a Python course on Udemy.

---

## 💻 Solution
```python
hour=16 
#hour=7 to print "Good Morning"  
if hour>=5 and hour<=11:
    print("Good Morning")
#current case hour=16  
elif hour>=12 and hour<=17:
    print("Good Afternoon")
#hour=20 to print "Good Evening"  
elif hour>=18 and hour<=21:
    print("Good Evening")
else:
#hour=23 to print "Good Night"    
    print("Good Night")
#the line below is printed always    
print("Greeting code has completed.")
