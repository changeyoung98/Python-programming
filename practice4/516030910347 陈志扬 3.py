# File: date2.py
# A program that outputs whether or not the date is valid and then calculates the corresponding day number
# By:Daisy
from string import *
def dayNum(m,d,y):
    if m>2:
        if y%400==0 or (y%100!=0 and y%4==0):
            dayNum=31*(m-1)+d-(4*m+23)/10+1
        else:
            dayNum=31*(m-1)+d-(4*m+23)/10
    else:
        dayNum=31*(m-1)+d
    print dayNum
def main():
    n=raw_input("Enter a date in the form month/day/year. ")
    a=find(n,"/")
    b=rfind(n,"/")
    m=eval(n[:a])
    d=eval(n[a+1:b])
    y=eval(n[b+1:])
    if m==4 or m==6 or m==9 or m==11:
        if 1<=d<=30:
            print ("valid")
            dayNum(m,d,y)
        else:
            print("invalid")
    elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        if 1<=d<=31:
            print ("valid")
            dayNum(m,d,y)
        else:
            print ("invalid")
    elif m==2:
        if y%400==0 and 1<=d<=29:
            print ("valid")
            dayNum(m,d,y)
        elif y%100!=0 and y%4==0 and 1<=d<=29:
            print("valid")
            dayNum(m,d,y)
        elif y%4!=0 and 1<=d<=28:
            print("valid")
            dayNum(m,d,y)
        else:
            print("invalid")
    else:
        print("invalid")
main()

