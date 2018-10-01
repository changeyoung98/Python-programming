# File: GCD.py
# A program that finds the GCD of two numbers
# By: Daisy
def GCD(n,m):
    n,m=m,n%m
    if m==0:
        return n
    else:
         return GCD(n,m)
def main():
    n,m=input("Enter two numbers divided by a comma. ")
    print GCD(n,m)

main()
