# File: count.py
# A program analyzes a file to determine the number of lines, words, and characters contained
# By:Daisy
import string
n=input("Enter the name of the file enclosed by double quotation marks: ")
f=open(n,"r")
numlines=len(f.readlines())
f=open("a.txt","r")
numwords=len(string.split(f.read()))
f=open("a.txt","r")
numchars=len(f.read())
print "The numbers of lines, words and characters are",numlines,numwords,numchars
