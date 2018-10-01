# -*- coding: cp936 -*-
# File:syracuse.py
# A program that gets a starting value from the user and then prints the Syracuse sequence for that starting value
# By:Daisy
def main():
    n=input("Enter the starting number（1 to quit）: ")
    print n,
    while n!=1:
        a=n%2
        if a==0:
            n=n/2
        else:
            n=3*n+1
        print n,

main()  
