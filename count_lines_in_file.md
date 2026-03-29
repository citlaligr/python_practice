# 🧠 Exercise: Count Lines in a File

## 📝 Problem
Work with file handling by reading a text file and calculating the number of lines it contains.

## Requirements
- Open a file named `file1.txt`.
- Read the file line by line.
- Count the total number of lines.
- Display the final count in the console.

## Expected Output
Total number of lines: 5

## Concepts Practiced
- File handling
- Iteration
- Counting logic
- Context managers (`with` statement)

## Source
Exercise inspired by a Python course on Udemy.

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
