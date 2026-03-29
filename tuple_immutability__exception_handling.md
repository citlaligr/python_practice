# 🧠 Exercise: Handle Tuple modification exception with Try Catch

## 📝 Problem

Create a tuple named person that contains three elements: a name (string), an age (integer), and a height (float) with the below values.

	- "Rahul"
	- 25
	- 5.9

Print the second element of the tuple.
Attempt to change the name in the tuple to a different name and explain why this will or will not work.


## 💻 Solution 

person=("Rahul", 25, 5.9)
print(f"Age: {person[1]}")


try:
    person[0] = "John"
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")