# File:prime.py
# A program that accepts a value of n as input and determines if the value is prime
# By: Daisy
def main():
    n=input("Enter the number to be decided(>2): ")
    for i in range(2,n):
        a=n%i
        if a==0:
            print("The number is not prime.")
            break
        else:
            if i==n-1:
                print("The number is prime.")
            else:
                continue

main()
