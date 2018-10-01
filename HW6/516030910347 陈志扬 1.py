# File: max.py
# A program to find the largest number in a list
# By: Daisy
def largest(s):
    if len(s)==1:
        return s[0]
    else:
        a=s[0]
        s.remove(a)
        b=largest(s)
        if a>=b:
            return a
        else:
            return b
def main():
    s=input("Enter the list to be decided. ")
    print largest(s)

main()
