# File:StatSet.py
# A class used to do simple statistical calculations
# By: Daisy
class StatSet:
    def __init__(self,statSet):
        self.statSet=[]
    def addNumber(self,x):
        self.statSet.append(x)
        return self.statSet
    def mean(self):
        s=0
        n=len(self.statSet)
        for i in self.statSet:
            s=s+i
        mean=s/float(n)
        return mean
    def median(self):
        s=self.statSet
        s.sort()
        n=len(self.statSet)
        if n%2==0:
            a=n/2-1
            b=n/2
            m=(s[a]+s[b])/2.0
        else:
            c=(n-1)/2
            m=s[c]
        return m
    def stdDev(self):
        n=len(self.statSet)
        m=StatSet(self.statSet).mean()
        s=0
        for i in range(n):
            s=s+(self.statSet[i]-m)**2
        d=s/n
        stdD=d**0.5
        return stdD
    def count(self):
        count=len(self.statSet)
        return count
    def _min(self):
        i=0
        a=self.statSet[0]
        for i in range(len(self.statSet)):
            if a>=self.statSet[i]:
                a=self.statSet[i]
        return a
    def _max(self):
        i=0
        a=self.statSet[0]
        for i in range(len(self.statSet)):
            if a<=self.statSet[i]:
                a=self.statSet[i]
        return a
