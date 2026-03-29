# 🧠 Exercise: Shopping Cart Validation

## 📝 Problem

Instructions:

Create a variable ItemsInCart and initialize it to 0.
Write a function called add_to_cart that accepts an integer parameter items_to_add.
If items_to_add is less than 0, raise an exception with the message "Cannot add a negative number of items."
If the total count of items after addition exceeds 5, raise an exception with the message "Cart limit exceeded."

# Example function structure
def add_to_cart(items_to_add):
    # Your code here
# Example of using the function

try:
    add_to_cart(2)  # Add 2 items
    add_to_cart(-1)  # This should raise an exception
except Exception as e:
    print(e)
	
## Expected Output 

2 items added. Total in cart: 2
Cannot add a negative number of items.

## 💻 Solution 

#create variable
ItemsInCart=0
#create a funcion that receive an integer parameter 
def add_to_cart(items_to_add):
    #define ItemsInCart as a global variable
    global ItemsInCart
    # if condition that can raise an exeption. Here we're considering only items_to_add  
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items")
    # elifif condition that can raise an exeption. Here we are considering the total count     
    elif items_to_add +ItemsInCart > 5:  
        raise Exception("Cart limit exceeded.")
    #It's the total of items in the cart, both the total and the new items added  
    ItemsInCart += items_to_add 
    #printing the total 
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")    
 
 
 
 
#Try/Except 

try:
    #Try to ejecute the function sending 2 as items_to_add. It will be print the total 
   add_to_cart(2)
   #Try to ejecute the function sending -1 as items_to_add. It will stop the flow and print the exeption
   add_to_cart(-1)
except Exception as e:
   #However if something happen that is not part of the exeption raised, the issue will be catched here    
   print(e)
