# File: futval.py
# A program to compute the value of an investment carried into the future
# By: Daisy
def main():
    print "This program calculates the future value of an investment."
    value = input("Enter the initial principal: ")
    apr = input("Enter the annualized interest rate: ")
    year=input("Enter the number of years of the investment: ")
    from string import *
    print center("Year",1),center("Value",23)
    print"-------------------------"
    print center("0",5),center("$%0.2f"% value,20)
    for i in range(year):
        value = value * (1 + apr)
        print " ",i+1,center("$%0.2f"% value,23)


main() 
