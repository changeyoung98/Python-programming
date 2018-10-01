# File: random_walk2.py
# A program to investigate how many steps away from the starting point you will end up in a random walk.
# By: Daisy
from random import randrange
def main():
    m=input("How many times do you want to try? ")
    n=input("Enter the number of the steps. ")
    s=0
    x=0
    y=0
    for i in range(m):
        for i in range(n):
            if randrange(1,5)==1:
                x=x+1
            elif randrange(1,5)==1:
                x=x-1
            elif randrange(1,5)==1:
                y=y+1
            else:
                y=y-1
        d=(x**2+y**2)**0.5        
        s=s+d
    a=float(s)/m
    print "The average ending distance is %0.1f"%(a)
main()
