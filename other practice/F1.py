# File: F1.py
from string import *
def main():
    n=input("Enter the number of players.")
    s=[0]*n
    s[0]=raw_input("In each row enter the entrance time and \
quitting time of one player divided by a space.\n")
    for i in range(1,n):
        s[i]=raw_input()
    for j in range(n):
        s[j]=split(s[j])
    for k in range(n):
        for l in range(n):
            a=s[k]
            b=s[l]
            if eval(a[0])<eval(b[0]):
                s[l]=a
                s[k]=b
    x=[0]
    y=[0]
    c=eval(s[0][0])
    d=eval(s[0][1])
    for m in range (n-1):
        p=m+1
        if d>eval(s[p][0]):
            if d>eval(s[p][1]):
                d=d
            else:
                d=eval(s[p][1])
        else:
            x.append(d-c)
            y.append(eval(s[p][0])-d)
            c=eval(s[p][0])
            d=eval(s[p][1])
    x.append(d-c)
    xmax=max(x)
    ymax=max(y)
    print xmax,ymax
            
                
main()
