# 🧠 Exercise: Average Calculator

## 📝 Problem

Objective: Calculate the average of three numbers.

Instructions:

Create a function called CalculateAverage that takes three parameters: num1, num2, and num3.
Use the numbers 10,20,30 as input to functions
The function should return the average of these three numbers.

## Expected Output 

The average of 10, 20, and 30 is 20.0

## 💻 Solution 

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