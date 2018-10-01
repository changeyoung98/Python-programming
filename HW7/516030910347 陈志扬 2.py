# File:13.py
# A program to count the times of each day in a week the 13th is on.
# By:Daisy
def dayNum(m,d,y):
    if m>2:
        if y%4==0 and (y%100!=0 or y%400==0):
            dayNum=31*(m-1)+d-(4*m+23)/10+1
        else:
            dayNum=31*(m-1)+d-(4*m+23)/10
    else:
        dayNum=31*(m-1)+d
    return dayNum
def leapNum(y):
    k=0
    for i in range(1900,y):
        if i%4==0 and (i%100!=0 or i%400==0):
            k=k+1
    return k
def day(m,d,y):
    Num=dayNum(m,d,y)+(y-1900)*365+leapNum(y)
    n=Num%7
    return n
def times(N):
    t1,t2,t3,t4,t5,t6,t7=0,0,0,0,0,0,0
    for y in range(1900,1900+N):
        for m in range(1,13):
            n=day(m,13,y)
            if n==1:
                t1=t1+1
            elif n==2:
                t2=t2+1
            elif n==3:
                t3=t3+1
            elif n==4:
                t4=t4+1
            elif n==5:
                t5=t5+1
            elif n==6:
                t6=t6+1
            else:
                t7=t7+1
    g=open("output.dat","w")
    g.write(str(t1)+" ")
    g.write(str(t2)+" ")
    g.write(str(t3)+" ")
    g.write(str(t4)+" ")
    g.write(str(t5)+" ")
    g.write(str(t6)+" ")
    g.write(str(t7)+" ")
    g.close
def main():
    f=open("input.dat","r")
    N=eval(f.read())
    times(N)
main()
