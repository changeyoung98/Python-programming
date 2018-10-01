# File: set.py
# Class set
# By: Daisy
class Set:
    def __init__(self,S):
        self.set=set(S)
    def addElement(self,x):
        s=[]
        for i in self.set:
            s.append(i)
        s.append(x)
        return set(s)
    def deleteElement(self,x):
        s=[]
        for i in self.set:
            s.append(i)
        for j in s:
            if j==x:
                s.remove(x)
        return set(s)
    def member(self,x):
        for i in self.set:
            if i==x:
                return True
        else:
            return False
    def intersection(self,set2):
        s=[]
        for i in self.set:
            for j in set2:
                if j==i:
                    s.append(j)
        return set(s)
    def union(self,set2):
        s1=[]
        for i in self.set:
            s1.append(i)
        s2=[]
        for j in set2:
            s2.append(j)
        s=s1+s2
        return set(s)
    def subtract(self,set2):
        s=[]
        for i in self.set:
            s.append(i)
        for j in self.set:
            for k in set2:
                if k==j:
                    s.remove(j)
        return set(s)
            
