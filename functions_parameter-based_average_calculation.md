# 🧠 Exercise: Function with Parameters - Average Calculation

## 📝 Problem
Practice creating functions that accept parameters and return calculated results.

## Requirements
- Define a function named `CalculateAverage` that takes three numeric parameters.
- Compute the average of the provided values.
- Return the calculated result.
- Call the function using sample values and display the output.

## Expected Output
The average of 10, 20, and 30 is 20.0

## Concepts Practiced
- Functions
- Parameters
- Return values
- Arithmetic operations

## Source
Exercise inspired by a Python course on Udemy.

## 💻 Solution 
```python
#Creation of a funcion where num1, num2, num3 are recieved as parameters
def CalculateAverage(num1, num2, num3):
    #new variable that is going to receive the average result
    avg = (num1 + num2 + num3) / 3      
    #the variable is sending back
    return avg
#Creation of the object where the function is instanced. The object send 10,20,30 as values.
prom=CalculateAverage(10,20,30)   
#Printing the result 
print(f"The average of 10, 20, and 30 is {prom}")
