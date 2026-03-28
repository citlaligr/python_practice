# 🧠 Exercise: Count Lines in a File

## 📝 Problem

Objective: Count and print the number of lines in a file.

Instructions:

Use the attached text file "file1.txt"
Write a Python script that opens the file, reads through it line by line, counts how many lines it has, and prints the total count.


## Expected Output 
Total number of lines: 5

## 💻 Solution 1
#This solution is better for big files

#Creating a file for total count
numberL = 0
#opening file and closing automatically
with open("file1.txt") as file:
#for each line in the file    
    for line in file:
#incrementing the total count
        numberL += 1
#printing total of lines
print(f"Total number of lines: {numberL}") 

## 💻 Solution 2
#This solution is better for small files

##opening file and closing automatically
with open("file1.txt") as file:
#using len to determine the size of the file considering the total of lines
    print (f"Total number of lines: {len(file.readlines())}")