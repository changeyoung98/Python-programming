# File: n.py
# A program to print
# By: Daisy
def add1(y,i,n):
    m=n/2
    x=eval(y)
    if i==0:
        x[m]=1
    elif 0<i<=m:
        x[m-i]=n-i+1
    else:
        x[n-i+m]=n-i+1
    a=[x]
    return a
def original(n):
    m=n/2
    a=[]
    x=[]
    for j in range(n):
        x=x+[0]
    y=str(x)
    for i in range(n):
        a=a+add1(y,i,n)
    return a
def add2(a,n):
    m=n/2
    k,l=2,m-1
    s=n**2+1
    for i in range(n+1,s):
        if k+1==0 and l-1==n-1:
            k,l=k+2,l-1
        else:
            if k==-1:
                k=n-1
            elif l==n:
                l=0
            else:
                if a[k][l]!=0:
                    k,l=k+2,l-1
                else:
                    k,l=k,l
        a[k][l]=i
        k,l=k-1,l+1
    return a
def main():
    n=input("Enter the rank of the list. ")
    m=n/2
    a=original(n)
    add2(a,n)
    print a

main()
