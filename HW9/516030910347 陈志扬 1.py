# Face.py
# A simple class that draws a face in a graphics window.
# By: Daisy
from graphics import *
class Face:
    def __init__(self,window,center,size):
        self.eyeSize=0.15*size
        self.eyeOff=size/3.0
        self.mouthSize=0.8*size
        self.mouthOff=size/2.0
        self.head=Circle(center,size)
        self.head.draw(window)
        self.leftEye=Circle(center,self.eyeSize)
        self.leftEye.move(-self.eyeOff,-self.eyeOff)
        self.rightEye=Circle(center,self.eyeSize)
        self.rightEye.move(self.eyeOff,-self.eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        self.window=window
        p1=center.clone()
        p2=center.clone()
        p1.move(-self.mouthSize/2,self.mouthOff)
        p2.move(self.mouthSize/2,self.mouthOff)
        self.mouth=Line(p1,p2)
        self.mouth.draw(self.window)
        p3=center.clone()
        p4=center.clone()
        self.bow1=Line(p3,p4)
        self.bow1.undraw()
        self.bow2=Line(p3,p4)
        self.bow2.undraw()
    def happy(self,center):
        self.bow1.undraw()
        self.bow2.undraw()
        self.mouth.undraw()
        p1=center.clone()
        p1.move(-self.mouthSize/2,self.mouthOff-10)
        p2=center.clone()
        p2.move(self.mouthSize/2,self.mouthOff-10)
        p3=center.clone()
        p3.move(-self.mouthSize/3,self.mouthOff+10)
        p4=center.clone()
        p4.move(self.mouthSize/3,self.mouthOff+10)
        self.mouth=Polygon(p1,p2,p4,p3)
        self.mouth.draw(self.window)
        p5=center.clone()
        p6=center.clone()
        self.bow1=Line(p5,p6)
        self.bow1.undraw()
        self.bow2=Line(p5,p6)
        self.bow2.undraw()
    def angry(self,center):
        self.bow1.undraw()
        self.bow2.undraw()
        self.mouth.undraw()
        p1=center.clone()
        p1.move(-self.mouthSize/2,self.mouthOff+10)
        p2=center.clone()
        p2.move(self.mouthSize/2,self.mouthOff+10)
        p3=center.clone()
        p3.move(0,self.mouthOff-10)
        self.mouth=Polygon(p1,p3,p2)
        self.mouth.draw(self.window)
        Line(p1,p2).undraw()
        p4=center.clone()
        p4.move(-self.mouthSize/2,-self.eyeOff*2)
        p5=center.clone()
        p5.move(-self.mouthSize/4,-self.eyeOff-5)
        self.bow1=Line(p5,p4)
        self.bow1.draw(self.window)
        p6=center.clone()
        p6.move(self.mouthSize/2,-self.eyeOff*2)
        p7=center.clone()
        p7.move(self.mouthSize/4,-self.eyeOff-5)
        self.bow2=Line(p6,p7)
        self.bow2.draw(self.window)
    def surprised(self,center):
        self.bow1.undraw()
        self.bow2.undraw()
        self.mouth.undraw()
        p3=center.clone()
        p3.move(0,self.mouthOff-10)
        self.mouth=Circle(p3,self.eyeSize)
        self.mouth.draw(self.window)
        p4=center.clone()
        p5=center.clone()
        self.bow1=Line(p4,p5)
        self.bow1.undraw()
        self.bow2=Line(p4,p5)
        self.bow2.undraw()
class Button:
    def __init__(self, window, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(window)
        self.label = Text(center, label)
        self.label.draw(window)
        
    def clicked(self, p):
          if self.xmin <= p.getX() <= self.xmax and \
             self.ymin <= p.getY() <= self.ymax:
              return True
            
def main():
    window=GraphWin('Face',320,240)
    center=Point(100,100)
    size=80
    a=Face(window,center,size)
    b1=Button(window,Point(40,210),70,35,'quit')
    b2=Button(window,Point(280,40),70,35,'happy')
    b3=Button(window,Point(280,120),70,35,'angry')
    b4=Button(window,Point(280,200),70,35,'surprized')
    p=window.getMouse()
    while not b1.clicked(p):
        if b2.clicked(p):
            a.happy(center)
        elif b3.clicked(p):
            a.angry(center)
        elif b4.clicked(p):
            a.surprised(center)
        p=window.getMouse()
    window.close()
    
main()
    
