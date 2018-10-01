# File:chaos2.py
# A simple program illustrating chaotic behaviour
# By:Chen Zhiyang
def main():
    print"This program illustrates a chaotic function"
    x,y=input("Enter two numbers between 0 and 1: ")
    for i in range(10):
        x=3.0*x*(1-x)
        y=3.0*y*(1-y)
        print x,y


main()
