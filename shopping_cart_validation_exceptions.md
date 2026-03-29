# 🧠 Exercise: Shopping Cart Validation

## 📝 Problem
Simulate a simple shopping cart system with validation rules to control item additions.

## Requirements
- Initialize a variable `items_in_cart` with a value of 0.
- Create a function `add_to_cart` that receives the number of items to add.
- Validate the following conditions:
  - Do not allow negative values.
  - Limit the total number of items in the cart to a maximum of 5.
- Raise appropriate exceptions when validation rules are violated.
- Display the updated cart status when items are successfully added.

## Expected Output
2 items added. Total in cart: 2  
Cannot add a negative number of items.

## Concepts Practiced
- Functions
- Parameters
- Global variables
- Conditional statements
- Exception handling

## Source
Exercise inspired by a Python course on Udemy.

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
