# File:sum.py
# A program to sum a series of numbers.
# Author:Chen Zhiyang
n=input("How many numbers are to be summed? ")
fact=0
for f in range(n):
    f=input("Enter one of the numbers to be summed. ")
    fact=fact+f
print"The sum is",fact
