# File:Fibonacci(1).py
# A program that computes the nth Fibonacci number.
# Author:Chen Zhiyang
n=input("Enter the ordinal number of the Fibonacci number: ")
x,y=0,1
for f in range(n):
    x,y=y,x+y,
    f=x
print"The",n,"th Fibonacci number is",f
