# File:count.py
# By:Daisy
from string import *
def count_words(ss,dd):
    s=split(ss)
    S=set(s)
    for i in S:
        if dd.has_key(i):
            dd[i]=dd[i]+s.count(i)
        else:
            dd[i]=s.count(i)
    return dd
def dict_sort(dd):
    s=[]
    s1=dd.items()
    n=len(s1)
    a=0
    while a<n:
        for i in range(a,n):
            if s1[i][1]>=s1[a][1]:
                s1[a],s1[i]=s1[i],s1[a]
        a=a+1
    ss=[]
    for j in s1:
        ss.append(j[0])
    return ss
        
                
        
def main():
    n=raw_input("Enter a file: ")
    f=open(n,"r")
    l=f.readlines()
    dd=dict()
    for i in range(len(l)):
        ss=l[i]
        dd=count_words(ss,dd)
    s=dict_sort(dd)
    print s
main()
        
