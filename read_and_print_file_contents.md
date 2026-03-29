# 🧠 Exercise: File Reading and Output

## 📝 Problem
Work with file handling by reading and displaying the contents of a text file.

## Requirements
- Open a file named `myfile.txt`.
- Read all its contents.
- Display the content in the console.

## Expected Behavior
- The program should print the full content of the file without modifications.

## Concepts Practiced
- File handling
- Reading files
- Input/Output operations

## Source
Exercise inspired by a Python course on Udemy.


## 💻 Solution
```python
#opening the file and asign to an object
file = open("myfile.txt")
#print the file with the function read()
print(file.read())
#after open any file, always close it
file.close()
