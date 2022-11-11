Create a Python function that calculates the hypotenuse of a triangle using Pythagorean Theorem. 
from math import sqrt
from tkinter import *

root = Tk()
root.title("Pythagorean Theorem Calculator")
root.geometry("450x250")

ValueLabel = Label(root, text="First leg length: ").pack()
e1 = Entry(root, width=25)
e1.pack()
ValueLabel2 = Label(root, text="Second leg length: ").pack()
e2 = Entry(root, width=25)
e2.pack()

answer = Entry(root, width=50)


def solve():
    value = float(e1.get())
    value2 = float(e2.get())
    hypotenuse = sqrt((value**2)+(value2**2))
    answer.delete(0, "end")
    answer.insert(0, "The lenght of the hypotenuse is " + str(round(hypotenuse, 3)) + " units long!")

solveButton = Button(root, text="Solve!", command=solve)
solveButton.pack()

answer.pack()

mainloop()




From the foobar.txt file posted on slack create a function that:
# open the file using open() function
file = open("sample.txt")
   
# Reading from file
print(file.read())
 
# closing the file
file.close()




Import the following library fibo and only import the following function: fib
# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
if __name__ == "__main__":
    n = 9
    print(fibonacci(n))




Create a function using the sys library that takes in two arguments from the user and prints both arguments out. 
# Python program to demonstrate
# sys.argv
  
  
import sys
  
  
print("This is the name of the program:",
       sys.argv[0])
print("Number of elements including the name of the program:",
       len(sys.argv))
print("Number of elements excluding the name of the program:",
      (len(sys.argv)-1))
print("Argument List:",
       str(sys.argv))

