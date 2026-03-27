# 🧠 Exercise: 

## 📝 Problem

Create a variable user and assign the value 16
Use if-elif-else statements to print:
	"Good Morning" if the hour is between 5 and 11,
	"Good Afternoon" if the hour is between 12 and 17,
	"Good Evening" if the hour is between 18 and 21,
	"Good Night" for all other hours.
Print "Greeting code has completed."

## Expected Output 
For input 10:
	Good Morning
	Greeting code has completed.

For input 15:
	Good Afternoon
	Greeting code has completed.

---

## 💻 Solution
```python
user=16 
#user=7 to print "Good Morning"  
if user>=5 and user<=11:
    print("Good Morning")
#current case user=16  
elif user>=12 and user<=17:
    print("Good Afternoon")
#user=20 to print "Good Evening"  
elif user>=18 and user<=21:
    print("Good Evening")
else:
#user=23 to print "Good Night"    
    print("Good Night")
#the line below is printed always    
print("Greeting code has completed.")