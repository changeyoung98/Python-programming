# File:random_walk.py
# A program to investigate how many steps away from the starting point you will end up in a random walk.
# By: Daisy
from random import randrange
def main():
    m=input("How many times do you want to try? ")
    n=input("Enter the number of the steps. ")
    s=0
    d=0
    for i in range(m):
        for i in range(n):
            if randrange(1,3)==1:
                d=d+1
            else:
                d=d-1
        s=s+d
    a=float(s)/m
    print "Suppose walking forward is '+'.The average ending distance is %0.1f"%(a)
main()
