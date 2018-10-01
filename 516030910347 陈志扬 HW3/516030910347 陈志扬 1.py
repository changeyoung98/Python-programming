# File:code.py
# A program that can encode and decode Caesar ciphers
# By:Daisy
message=raw_input("Enter the message to encode: ")
n=input("What is the key value? ")
code=""
for ch in message:
    code=code+chr(ord(ch)+n)
print("The code is"),code
