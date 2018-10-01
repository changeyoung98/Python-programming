# File: array.py
# A program that prints arrays
# By: Daisy
def main():
    a=[]
    c=input("Enter the length of the array: ")
    for k in range(c):
        a=a+[0]
    print a
    for b in a:
        print b
    x=[]
    y=[]
    m,n=input("Enter the lengths of the array(in the form of 'row,line'): ")
    for j in range(n):
        x=x+[0]
    for i in range(m):
        y=y+[x]
    print y
    for s in range(m):
        for t in range(n):
            print y[s][t]

main()
