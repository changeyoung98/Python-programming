# File:clock.py
# By:Daisy
class Clock:
    def __init__(self,h=0,m=0,s=0):
        self.hour=h
        self.minute=m
        self.second=s
    def getTime(self):
        return (self.hour,self.minute,self.second)
    def __add__(self,c2):
        h=self.hour+c2.hour
        m=self.minute+c2.minute
        s=self.second+c2.second
        return Clock(h,m,s)
    def  __str__(self):
        return "(%d:%d:%d)"%self.getTime()
def main():
    c1=Clock(10,20,30)
    c2=Clock(1,2,3)
    c3=c1+c2
    print c3
main()
