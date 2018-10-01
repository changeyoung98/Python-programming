# File: Palindrome.py
# A program to decide whether a number is Palindrome number.
# By: Daisy
def is_Palindrome_number(n):
    m=''
    for i in range(len(n)):
        m=m+n[len(n)-i-1]
    if m==n:
        print("True.")
    else:
        print("False.")
def main():
    n=raw_input("Enter the number to be decided. ")
    is_Palindrome_number(n)

main()
