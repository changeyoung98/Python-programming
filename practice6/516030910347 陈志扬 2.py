# File: list.py
# An algorithm for each of some Python operations
# By: Daisy
class _list():
    def __init__(self,myList):
        self.List=myList
    def count(self,x):
        i=0
        for j in self.List:
            if j==x:
                i=i+1
        return i
    def isin(self,x):
        for i in self.List:
            if i==x:
                return True
            else:
                return False

    def index(self,x):
        i=0
        for j in self.List:
            if j==x:
                return i
            i=i+1
    def reverse(self):
        n=len(self.List)
        s=[0]*n
        for i in range(n):
            s[i]=self.List[n-i-1]
        return s
    def sort(self):
        for j in range(len(self.List)):
            for i in range(len(self.List)):
                a=self.List[j]
                b=self.List[i]
                if a<b:
                    self.List[i]=a
                    self.List[j]=b
        return self.List
def main():
    myList=input("Enter a list. ")
    x=input("Enter the element. ")
    print _list(myList).count(x)
    print _list(myList).isin(x)
    print _list(myList).index(x)
    print _list(myList).reverse()
    print _list(myList).sort()
                
main()
