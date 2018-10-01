# ATM.py
# A program that simulates an ATM
# By:Daisy
from graphics import *
from string import*
win=GraphWin('ATM',640,480)
f= open("account.txt","r")

class Button:
    def __init__(self, win, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax,self.xmin=x+w,x-w
        self.ymax,self.ymin=y+h,y-h
        p1=Point(self.xmin,self.ymin)
        p2=Point(self.xmax,self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

    def clicked(self, p):
        if self.xmin <= p.getX() <= self.xmax and \
           self.ymin <= p.getY() <= self.ymax:
            return True
    def _undraw(self):
        self.rect.undraw()
        self.label.undraw()

def _ID():
    t1=Text(Point(300,200),'ID')
    t1.draw(win)
    return t1
def _PIN():
    t2=Text(Point(300,300),'PIN')
    t2.draw(win)
    return t2

def getID():
    ID=Entry(Point(350,200),5)
    ID.draw(win)
    return ID
def getPIN():
    PIN=Entry(Point(350,300),5)
    PIN.draw(win)
    return PIN
class _Enter:
    def __init__(self,win):
        self.win=win
        self.c1=Text(Point(320,200),'')
        self.c2=Entry(Point(320,300),'')
        self.c3=Button(self.win,Point(320,400),100,30,'Click to enter')
        self.c4=Text(Point(320,200),'')
        self.c5=Entry(Point(320,300),'')
        self.c1.undraw()
        self.c2.undraw()
        self.c3._undraw()
        self.c4.undraw()
        self.c5.undraw()
    def _check(self,s,i):
        self.c1.undraw()
        self.c2.undraw()
        self.c3._undraw()
        self.c4.undraw()
        self.c5.undraw()
        t1=s[i+2]
        t2=s[i+3]
        self.c1=Text(Point(280,200),'Your checking account balance is ')
        self.c1.draw(self.win)
        self.c2=Entry(Point(450,200),8)
        self.c2.setText(t1)
        self.c2.draw(self.win)
        self.c4=Text(Point(280,300),'Your savings account balance is ')
        self.c4.draw(self.win)
        self.c5=Entry(Point(450,300),8)
        self.c5.setText(t2)
        self.c5.draw(self.win)
        
    def _withdraw(self,s,i):
        self.c1.undraw()
        self.c2.undraw()
        self.c3._undraw()
        self.c4.undraw()
        self.c5.undraw()
        self.c1=Text(Point(320,200),'Please enter the amount')
        self.c1.draw(self.win)
        self.c2=Entry(Point(320,300),10)
        self.c2.draw(self.win)
        self.c3=Button(self.win,Point(320,400),100,30,'Click to enter')
        p=self.win.getMouse()
        m=self.c2.getText()
        if self.c3.clicked(p) and m!='':
            if eval(m)<=eval(s[i+2]):
                return eval(m)
            else:
                self.c3._undraw()
                self.c3=Button(self.win,Point(320,400),250,30,'Not sufficient funds,please check')
                m=0
                return m
        else:
            m=0
            return m
    def _deposit(self,s,i):
        self.c1.undraw()
        self.c2.undraw()
        self.c3._undraw()
        self.c4.undraw()
        self.c5.undraw()
        self.c1=Text(Point(320,200),'Please enter the amount')
        self.c1.draw(self.win)
        self.c2=Entry(Point(320,300),10)
        self.c2.draw(self.win)
        self.c3=Button(self.win,Point(320,400),100,30,'Click to enter')
        p=self.win.getMouse()
        m=self.c2.getText()
        if self.c3.clicked(p) and m!='':
            return eval(m)
        else:
            m=0
            return m
    def _transfer(self,s,i):
        self.c1.undraw()
        self.c2.undraw()
        self.c3._undraw()
        self.c4.undraw()
        self.c5.undraw()
        self.c1=Text(Point(260,200),'Please enter the amount(savings to checking)')
        self.c1.draw(self.win)
        self.c2=Entry(Point(480,200),10)
        self.c2.draw(self.win)
        self.c4=Text(Point(260,300),'Please enter the amount(checking to saving)')
        self.c4.draw(self.win)
        self.c5=Entry(Point(480,300),10)
        self.c5.draw(self.win)
        self.c3=Button(self.win,Point(320,400),100,30,'Click to enter')
        p=self.win.getMouse()
        m1=self.c2.getText()
        m2=self.c5.getText()
        if self.c3.clicked(p):
            if m1!='':
                if eval(m1)<=eval(s[i+3]):
                    return eval(m1)
                else:
                    self.c3._undraw()
                    self.c3=Button(self.win,Point(320,400),250,30,'Not sufficient funds,please check')
                    m=0
                    return m
            elif m2!='':
                if eval(m2)<=eval(s[i+2]):
                    return -eval(m2)
                else:
                    self.c3._undraw()
                    self.c3=Button(self.win,Point(320,400),250,30,'Not sufficient funds,please check')
                    m=0
                    return m
            else:
                m=0
                return m
        else:
            m=0
            return m

    
def main():
    s=split(f.read())
    t1=_ID()
    t2=_PIN()
    b0=Button(win,Point(320,400),50,30,'Enter')
    ID=getID()
    PIN=getPIN()
    p=win.getMouse()
    a1=ID.getText()
    a2=PIN.getText()
    i=s.index(a1)
    if i+1==s.index(a2) and \
       b0.clicked(p):
        b0._undraw()
        t1.undraw()
        t2.undraw()
        ID.undraw()
        PIN.undraw()
        b1=Button(win,Point(50,50),50,30,'check')
        b2=Button(win,Point(50,250),70,30,'withdraw')
        b3=Button(win,Point(50,450),55,30,'deposit')
        b4=Button(win,Point(600,200),60,30,'transfer')
        b5=Button(win,Point(600,440),50,30,'quit')
    c=_Enter(win)
    pt=win.getMouse()
    while not b5.clicked(pt):
        if b1.clicked(pt):
            c._check(s,i)
        elif b2.clicked(pt):
            m=c._withdraw(s,i)
            m1=eval(s[i+2])-m
            s[i+2]=str(m1)
        elif b3.clicked(pt):
            m=c._deposit(s,i)
            m2=eval(s[i+2])+m
            s[i+2]=str(m2)
        elif b4.clicked(pt):
            m=c._transfer(s,i)
            m3=eval(s[i+2])+m
            m4=eval(s[i+3])-m
            s[i+2]=str(m3)
            s[i+3]=str(m4)
        pt=win.getMouse()   
    win.close()
    t=''
    for j in range(len(s)):
        t=t+s[j]
        t=t+' '
    g=open("account.txt","w")
    g.write(t)


main()
