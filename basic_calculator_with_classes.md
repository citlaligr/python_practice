# 🧠 Exercise: Understanding class creation in Python

## 📝 Problem

Objective: Create a basic calculator class to perform addition, subtraction, multiplication, and division.

Instructions:

Create a class named BasicCalculator.
Define a constructor that initializes two numbers. Use numbers 10 & 5
Implement methods for:

	- Addition
	- Subtraction
	- Multiplication
	- Division

Each method should return the result of the operation.

Create an instance of the BasicCalculator class and demonstrate the functionality of each method.


## Expected Output 

Addition: 10 + 5 = 15
Subtraction: 10 - 5 = 5
Multiplication: 10 * 5 = 50
Division: 10 / 5 = 2.0

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