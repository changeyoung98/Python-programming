# File: balance.py
# A program to find the balance point of a list.
# By: Daisy
def find_balance_point(A):
    i,j=0,len(A)-1
    x=A[i]
    y=A[j]
    while i<j:
        if i+2==j:
            if x==y:
                print "The index of the element is",i+1
                break
            else:
                print "-1"
                break
        else:
            if x<y:
                x=x+A[i+1]
                i=i+1
            else:
                y=y+A[j-1]
                j=j-1
def main():
    A=input("Enter the list. ")
    find_balance_point(A)

main()
