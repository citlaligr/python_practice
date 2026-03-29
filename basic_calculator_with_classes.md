# 🧠 Exercise: Basic Calculator Class (OOP)

## 📝 Problem
Practice object-oriented programming by creating a class that performs basic arithmetic operations.

## Requirements
- Create a class named `BasicCalculator`.
- Define a constructor to initialize two numeric values.
- Implement methods for the following operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Each method should return the result of the operation.
- Create an instance of the class and demonstrate the use of each method.

## Expected Output
Addition: 10 + 5 = 15  
Subtraction: 10 - 5 = 5  
Multiplication: 10 * 5 = 50  
Division: 10 / 5 = 2.0  

## Concepts Practiced
- Classes and objects
- Constructors (`__init__`)
- Methods
- Object-oriented programming (OOP)

## Source
Exercise inspired by a Python course on Udemy.

## 💻 Solution

#Creating a class
class BasicCalculator:
    #Defining a constructor
    def __init__(self,a,b):
        #Initializing two numbers
        self.value1=a
        self.value2=b
    #Implementing Addition method 
    def addition(self):
        return self.value1 + self.value2 #math operation
    #Implementing Substraction method
    def subtraction(self):
         return self.value1 - self.value2
    #Implementing Multiplication method
    def multiplication(self):
        return self.value1 * self.value2
    #Implementing Division method
    def division(self):
        return self.value1 / self.value2

#creating an instance of the class         
value=BasicCalculator(10,5)

#printing results
print(f"Addition: {value.value1} + {value.value2} = {value.addition()}")
print(f"Subtraction: {value.value1} - {value.value2} = {value.subtraction()}")
print(f"Multiplication:{value.value1} * {value.value2} = {value.multiplication()}")
print(f"Division: {value.value1} / {value.value2} = {value.division()}")
