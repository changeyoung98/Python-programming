# File:quiz.py
# A program to draw a quiz score histogram
# By: Daisy
from string import *
from graphics import *
def main():
    n = raw_input("Enter the file name. ")
    f = open(n,"r")
    a=f.read()
    a=a.split()
    s=[]
    for i in range(11):
        c=a.count(str(i))
        s=s+[c]
    win=GraphWin("Quiz score",320,240)
    for i in range(11):
        m=50+20*i
        Text(Point(m,200),str(i)).draw(win)
        height=s[i]*10
        Rectangle(Point(m-8,180),(Point(m+8,180-height))).draw(win)
    
    
        

main()
