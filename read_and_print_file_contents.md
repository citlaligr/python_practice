# 🧠 Exercise: Read and Print File Contents

## 📝 Problem

Objective: Write a program to read the contents of a file and print it to the console.

Instructions:

Write a Python script that opens the file file1.txt and reads all its contents.
Print the entire content of the file.


## 💻 Solution

#opening the file and asign to an object
file = open("file1.txt")
#print the file with the function read()
print(file.read())
#after open any file, always close it
file.close()