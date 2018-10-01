# File:chaos.py
# A simple program illustrating chaotic behaviour
# By:Chen Zhiyang
def main():
    print"This program illustrates a chaotic function"
    x=input("Enter a number between 0 and 1: ")
    for i in range(20):
        x=3.0*x*(1-x)
        print x


main()
