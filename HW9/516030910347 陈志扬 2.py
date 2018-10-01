# File:face2.py
# A program that makes a face bounce around in a window
# By: Daisy
from graphics import *
from random import randrange
from time import sleep
class Face():
    def __init__(self,window,center,size):
        self.center=center
        self.window=window
        self.eyeSize=0.15*size
        self.eyeOff=size/3.0
        self.mouthSize=0.8*size
        self.mouthOff=size/2.0
        self.head=Circle(self.center,size)
        self.head.draw(self.window)
        self.leftEye=Circle(self.center,self.eyeSize)
        self.leftEye.move(-self.eyeOff,-self.eyeOff)
        self.rightEye=Circle(self.center,self.eyeSize)
        self.rightEye.move(self.eyeOff,-self.eyeOff)
        self.leftEye.draw(self.window)
        self.rightEye.draw(self.window)
        p1=self.center.clone()
        p2=self.center.clone()
        p1.move(-self.mouthSize/2,self.mouthOff)
        p2.move(self.mouthSize/2,self.mouthOff)
        self.mouth=Line(p1,p2)
        self.mouth.draw(self.window)
        p3=self.center.clone()
        p4=self.center.clone()
        self.bow1=Line(p3,p4)
        self.bow1.undraw()
        self.bow2=Line(p3,p4)
        self.bow2.undraw()
    def happy(self):
        self.bow1.undraw()
        self.bow2.undraw()
        self.mouth.undraw()
        p1=self.center.clone()
        p1.move(-self.mouthSize/2,self.mouthOff-10)
        p2=self.center.clone()
        p2.move(self.mouthSize/2,self.mouthOff-10)
        p3=self.center.clone()
        p3.move(-self.mouthSize/3,self.mouthOff+10)
        p4=self.center.clone()
        p4.move(self.mouthSize/3,self.mouthOff+10)
        self.mouth=Polygon(p1,p2,p4,p3)
        self.mouth.draw(self.window)
        p5=self.center.clone()
        p6=self.center.clone()
        self.bow1=Line(p5,p6)
        self.bow1.undraw()
        self.bow2=Line(p5,p6)
        self.bow2.undraw()
    def angry(self):
        self.bow1.undraw()
        self.bow2.undraw()
        self.mouth.undraw()
        p1=self.center.clone()
        p1.move(-self.mouthSize/2,self.mouthOff+10)
        p2=self.center.clone()
        p2.move(self.mouthSize/2,self.mouthOff+10)
        p3=self.center.clone()
        p3.move(0,self.mouthOff-10)
        self.mouth=Polygon(p1,p3,p2)
        self.mouth.draw(self.window)
        Line(p1,p2).undraw()
        p4=self.center.clone()
        p4.move(-self.mouthSize/2,-self.eyeOff*2)
        p5=self.center.clone()
        p5.move(-self.mouthSize/4,-self.eyeOff-5)
        self.bow1=Line(p5,p4)
        self.bow1.draw(self.window)
        p6=self.center.clone()
        p6.move(self.mouthSize/2,-self.eyeOff*2)
        p7=self.center.clone()
        p7.move(self.mouthSize/4,-self.eyeOff-5)
        self.bow2=Line(p6,p7)
        self.bow2.draw(self.window)
    def surprised(self):
        self.bow1.undraw()
        self.bow2.undraw()
        self.mouth.undraw()
        p3=self.center.clone()
        p3.move(0,self.mouthOff-10)
        self.mouth=Circle(p3,self.eyeSize)
        self.mouth.draw(self.window)
        p4=self.center.clone()
        p5=self.center.clone()
        self.bow1=Line(p4,p5)
        self.bow1.undraw()
        self.bow2=Line(p4,p5)
        self.bow2.undraw()
class move1(Face):
    def __init__(self,window,center,size):
        Face.__init__(self,window,center,size)
    def move(self,x,y):
        self.head.move(x,y)
        self.leftEye.move(x,y)
        self.rightEye.move(x,y)
        self.mouth.move(x,y)
        self.center.move(x,y)
        self.bow1.move(x,y)
        self.bow2.move(x,y)
    def undraw(self):
        self.head.undraw()
        self.leftEye.undraw()
        self.rightEye.undraw()
        self.mouth.undraw()
        self.center.undraw()
        self.bow1.undraw()
        self.bow2.undraw()
    def hit(self):
        if 560 <= self.center.getX() or \
           self.center.getX()<=80 or \
           400 <= self.center.getY() or\
           self.center.getY()<=80:
            return True
class move2(Face):
    def __init__(self,window,center,size):
        Face.__init__(self,window,center,size)
        Face.happy(self)
    def move(self,x,y):
        self.head.move(x,y)
        self.leftEye.move(x,y)
        self.rightEye.move(x,y)
        self.mouth.move(x,y)
        self.center.move(x,y)
        self.bow1.move(x,y)
        self.bow2.move(x,y)
    def undraw(self):
        self.head.undraw()
        self.leftEye.undraw()
        self.rightEye.undraw()
        self.mouth.undraw()
        self.center.undraw()
        self.bow1.undraw()
        self.bow2.undraw()
    def hit(self):
        if 560 <= self.center.getX() or \
           self.center.getX()<=80 or \
           400 <= self.center.getY() or\
           self.center.getY()<=80:
            return True
class move3(Face):
    def __init__(self,window,center,size):
        Face.__init__(self,window,center,size)
        Face.angry(self)
    def move(self,x,y):
        self.head.move(x,y)
        self.leftEye.move(x,y)
        self.rightEye.move(x,y)
        self.mouth.move(x,y)
        self.center.move(x,y)
        self.bow1.move(x,y)
        self.bow2.move(x,y)
    def undraw(self):
        self.head.undraw()
        self.leftEye.undraw()
        self.rightEye.undraw()
        self.mouth.undraw()
        self.center.undraw()
        self.bow1.undraw()
        self.bow2.undraw()
    def hit(self):
        if 560 <= self.center.getX() or \
           self.center.getX()<=80 or \
           400 <= self.center.getY() or\
           self.center.getY()<=80:
            return True
class move4(Face):
    def __init__(self,window,center,size):
        Face.__init__(self,window,center,size)
        Face.surprised(self)
    def move(self,x,y):
        self.head.move(x,y)
        self.leftEye.move(x,y)
        self.rightEye.move(x,y)
        self.mouth.move(x,y)
        self.center.move(x,y)
        self.bow1.move(x,y)
        self.bow2.move(x,y)
    def undraw(self):
        self.head.undraw()
        self.leftEye.undraw()
        self.rightEye.undraw()
        self.mouth.undraw()
        self.center.undraw()
        self.bow1.undraw()
        self.bow2.undraw()
    def hit(self):
        if 560 <= self.center.getX() or \
           self.center.getX()<=80 or \
           400 <= self.center.getY() or\
           self.center.getY()<=80:
            return True

def main():
    window=GraphWin('Face',640,480)
    center=Point(100,100)
    size=80
    x=randrange(-10,10)
    y=randrange(-10,10)
    m=["move1(window,center,size)","move2(window,center,size)","move3(window,center,size)","move4(window,center,size)"]
    i=0
    a=move1(window,center,size)
    while True:
        j=i%4
        k=(i+1)%4
        if not a.hit():
            a.move(x,y)
            sleep(0.1)
        elif 560 <= center.getX() or \
           center.getX()<=80 :
            a.undraw()
            a=eval(m[k])
            a.move(-x,y)
            x=-x
            i=i+1
        else:
            a.undraw()
            a=eval(m[k])
            a.move(x,-y)
            y=-y
            i=i+1

    window.getMouse()    
    window.close()

main()
