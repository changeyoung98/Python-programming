# -*- coding: utf-8 -*-
from graphics import *
from random import *
class square:
    def __init__(self,win,center,colour,chara):
        w,h=20,20
        x,y=center.getX(),center.getY()
        self.xmax,self.xmin=x+w,x-w
        self.ymax,self.ymin=y+h,y-h
        p1=Point(self.xmin,self.ymin)
        p2=Point(self.xmax,self.ymax)
        self.rect=Rectangle(p1,p2)
        self.rect.setFill(colour)
        self.rect.draw(win)
        self.text=Text(center,chara)
        self.text.draw(win)
        self.deactivated()
    def clicked(self,p):
        return self.xmin<=p.getX()<=self.xmax and \
               self.ymin<=p.getY()<=self.ymax
    def disappear(self):
        self.rect.undraw()
        self.text.undraw()
    def isactive(self):
        return self.active
    def activated(self):
        self.rect.setWidth(2)
        self.active=True
    def deactivated(self):
        self.rect.setWidth(1)
        self.active=False
    
class Button:
    def __init__(self,win,center,width,height,label):
        self.win=win
        w,h=width/2.0,height/2.0
        x,y=center.getX(),center.getY()
        self.xmax,self.xmin=x+w,x-w
        self.ymax,self.ymin=y+h,y-h
        p1=Point(self.xmin,self.ymin)
        p2=Point(self.xmax,self.ymax)
        self.rect=Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(self.win)
        self.label=Text(center, label)
        self.label.draw(self.win)

    def clicked(self,p):
        return self.xmin<=p.getX()<=self.xmax and \
               self.ymin<=p.getY()<=self.ymax
    def _undraw(self):
        self.rect.undraw()
        self.label.undraw()
class catalog:
    def __init__(self):
        self.win=GraphWin('Colour & Poems',640,480)
    def click(self):
        self.t=Text(Point(320,150),'Welcome to the game!')
        self.t.setSize(30)
        self.t.draw(self.win)
        self.b1=Button(self.win,Point(320,240),80,30,'Introduction')
        self.b2=Button(self.win,Point(320,320),80,30,'Play')
        self.b3=Button(self.win,Point(320,400),80,30,'Quit')
        self.b4=Button(self.win,Point(320,400),80,30,'')
        self.b5=Button(self.win,Point(320,400),80,30,'')
        self.b4._undraw()
        self.b5._undraw()
        p=self.win.getMouse()
        while not self.b3.clicked(p):
            if self.b1.clicked(p):
                self.t.undraw()
                self.b1._undraw()
                self.b2._undraw()
                self.b3._undraw()
                try:
                    self.intro()
                except GraphicsError:
                    pass
            elif self.b2.clicked(p):
                self.t.undraw()
                self.b1._undraw()
                self.b2._undraw()
                self.b3._undraw()
                try:
                    self.play()
                except GraphicsError:
                    pass
            p=self.win.getMouse()
        if self.b3.clicked(p):
            self.win.close()
    def intro(self):
        self.t.undraw()
        self.b1._undraw()
        self.b2._undraw()
        self.b3._undraw()
        self.b2=Button(self.win,Point(320,100),600,30,\
                       'Click two squares to get their colour exchanged.')
        self.b3=Button(self.win,Point(320,220),600,30,'Make sure \
the characters in one sentence are in the same colour.')
        self.t=Button(self.win,Point(320,340),600,30,'Enter the \
poem by clicking the characters in the right order')
        self.b1=Button(self.win,Point(600,450),50,30,'Return')
        pt=self.win.getMouse()
        while not self.b1.clicked(pt):
            pt=self.win.getMouse()
        else:
            self.t._undraw()
            self.b2._undraw()
            self.b3._undraw()
            self.b1._undraw()
            try:
                self.click()
            except GraphicsError:
                pass
    def play(self):
        self.t.undraw()
        self.b1._undraw()
        self.b2._undraw()
        self.b3._undraw()
        self.b1=Button(self.win,Point(100,240),90,30,'yellow')
        self.b2=Button(self.win,Point(260,240),90,30,'green')
        self.b3=Button(self.win,Point(420,240),90,30,'blue')
        self.b5=Button(self.win,Point(580,240),90,30,'pink')
        self.b4=Button(self.win,Point(600,450),50,30,'Return')
        ps=self.win.getMouse()
        while not self.b4.clicked(ps):
            if self.b1.clicked(ps):
                self.b1._undraw()
                self.b2._undraw()
                self.b3._undraw()
                self.b4._undraw()
                self.b5._undraw()
                self.yellow()
            elif self.b2.clicked(ps):
                self.b1._undraw()
                self.b2._undraw()
                self.b3._undraw()
                self.b4._undraw()
                self.b5._undraw()
                self.green()
            elif self.b3.clicked(ps):
                self.b1._undraw()
                self.b2._undraw()
                self.b3._undraw()
                self.b4._undraw()
                self.b5._undraw()
                self.blue()
            elif self.b5.clicked(ps):
                self.b1._undraw()
                self.b2._undraw()
                self.b3._undraw()
                self.b4._undraw()
                self.b5._undraw()
                self.pink()
            else:
                ps=self.win.getMouse()
        else:
            self.t.undraw()
            self.b1._undraw()
            self.b2._undraw()
            self.b3._undraw()
            self.b4._undraw()
            self.b5._undraw()
            try:
                self.click()
            except GraphicsError:
                pass
    def yellow(self):
        s=[0]*48
        t=['khaki']*12+['wheat']*12+['beige']*12+['yellow']*12
        v,w=poem()
        u=v
        shuffle(t)
        shuffle(u)
        self.process(s,t,u,v,w)
    def process(self,s,t,u,v,w):
        for i in range(48):
            x=(i%8)*40+100
            y=(i/8)*40+100
            colour=t[i]
            chara=u[i]
            s[i]=square(self.win,Point(x,y),colour,chara)
        b1=Button(self.win,Point(600,450),70,30,'return')
        b2=Button(self.win,Point(600,400),70,30,'enter')
        p=self.win.getMouse()
        while not b1.clicked(p) and (not b2.clicked(p)):
            for i in range(48):
                if s[i].clicked(p):
                    s[i].activated()
                    p=self.win.getMouse()
                    while (not b1.clicked(p)) and s[i].isactive():
                        for h in range(48):
                            if s[h].clicked(p):
                                if h==i:
                                    s[i].deactivated()
                                else:
                                    s[i].deactivated()
                                    s[i].disappear()
                                    s[h].disappear()
                                    x1=(i%8)*40+100
                                    y1=(i/8)*40+100
                                    colour1=t[i]
                                    chara1=u[i]
                                    x2=(h%8)*40+100
                                    y2=(h/8)*40+100
                                    colour2=t[h]
                                    chara2=u[h]
                                    s[i]=square(self.win,Point(x1,y1),colour2,chara1)
                                    s[h]=square(self.win,Point(x2,y2),colour1,chara2)
                                    t[i]=colour2
                                    t[h]=colour1
                        else:
                            p=self.win.getMouse()
            p=self.win.getMouse()
        while not b1.clicked(p):
            if b2.clicked(p):
                b2._undraw()
                b3=Button(self.win,Point(600,400),70,30,'yes')
                b5=Button(self.win,Point(600,350),70,30,'delete')
                T=Text(Point(320,380),"")
                T.draw(self.win)
                p=self.win.getMouse()
                sentence=""
                Colours=[]
                while not b1.clicked(p) and (not b3.clicked(p)):
                    for k in range(48):
                        if s[k].clicked(p):
                            sentence=sentence+u[k]
                            Colours=Colours+[t[k]]
                            T.setText(sentence)
                    if b5.clicked(p):
                        sentence=sentence[:-3]
                        Colours=Colours[:-1]
                        T.setText(sentence)
                    p=self.win.getMouse()
                if b3.clicked(p):
                    text1=T.getText()
                    text2=w[0]
                    for m in range(48):
                        s[m].disappear()
                    b3._undraw()
                    b5._undraw()
                    T.undraw()
                    if right(text1,text2,Colours,w[1:]):
                        T=Text(Point(320,200),"YOU WIN!")
                        T.setStyle('bold')
                        T.setSize(30)
                        T.draw(self.win)
                        b4=Button(self.win,Point(600,400),70,30,'next')
                        p=self.win.getMouse()
                        while not b1.clicked(p):
                            if b4.clicked(p):
                                T.undraw()
                                b1._undraw()
                                b4._undraw()
                                self.play()
                            p=self.win.getMouse()
                        else:
                            T.undraw()
                            b1._undraw()
                            b4._undraw()
                            self.play()
                            
                    else:
                        T=Text(Point(320,200),"SORRY! YOU LOSE")
                        T.setStyle('bold')
                        T.setSize(30)
                        T.draw(self.win)
                        p=self.win.getMouse()
                        while not b1.clicked(p):
                            p=self.win.getMouse()
                        else:
                            T.undraw()
                            b1._undraw()
                            self.play()
                else:
                    for j in range(48):
                        s[j].disappear()
                    T.undraw()
                    b1._undraw()
                    b3._undraw()
                    b5._undraw()
                    self.play()
        else:
            for j in range(48):
                s[j].disappear()
            b1._undraw()
            b2._undraw()
            self.click()
    def green(self):
        s=[0]*48
        t=['darkgreen']*8+['palegreen']*8+['yellowgreen']*8+\
           ['turquoise']*8+['seagreen']*8+['green']*8
        v,w=poem()
        u=v
        shuffle(t)
        shuffle(u)
        self.process(s,t,u,v,w)
    def blue(self):
        s=[0]*48
        t=['blue']*8+['steelblue']*8+['skyblue']*8+\
           ['royalblue']*8+['darkblue']*8+['lightblue']*8
        v,w=poem()
        u=v
        shuffle(t)
        shuffle(u)
        self.process(s,t,u,v,w)
    def pink(self):
        s=[0]*48
        t=['pink']*8+['plum']*8+['violet']*8+['peachpuff']*12+['palevioletred']*12
        v,w=poem()
        u=v
        shuffle(t)
        shuffle(u)
        self.process(s,t,u,v,w)

def right(text1,text2,Colours,w):
    c=[0]*len(w)
    m=0
    for i in range (len(w)):
        n=m+w[i]
        c[i]=Colours[m:n]
        m=n
    if text1==text2:
        for j in c:
            s=set(j)
            if len(s)!=1:
                return False
        else:
            t=set(Colours)
            if len(t)==len(w):
                return True
            else:
                return False
    else:
        return False

def poem():
    s=[0]*10
    r=[0]*10
    s[0]=["零","落","成","泥","碾","作","尘","只","有",\
          "香","如","故","月","暗","为","无","木","影"]+['']*30
    r[0]=["零落成泥碾作尘只有香如故",7,5]
    s[1]=['而','今','识','得','愁','滋','味','欲',\
          '说','还','休','欲','说','还','休','却',\
          '道','天','凉','好','个','秋','将','恰','君','相','笑','意']+['']*20
    r[1]=["而今识得愁滋味欲说还休欲说还休却道天凉好个秋",7,4,4,7]
    s[2]=['竹','杖','芒','鞋','轻','胜','马','谁',\
          '怕','一','蓑','烟','雨','任','平','生',\
          '白','骑','濛','雪','笠','愿','翠','微']+['']*24
    r[2]=["竹杖芒鞋轻胜马谁怕一蓑烟雨任平生",7,2,7]
    s[3]=['明','月','楼','高','休','独','倚','酒',\
          '入','愁','肠','化','作','相','思','泪',\
          '何','照','伫','风','细','断','涯','登']+['']*24
    r[3]=["明月楼高休独倚酒入愁肠化作相思泪",7,4,5]
    s[4]=['今','宵','酒','醒','何','处','杨','柳',\
          '岸','晓','风','残','月','依','春','短',\
          '面','醉','花','凄','飒','雨']+['']*26
    r[4]=["今宵酒醒何处杨柳岸晓风残月",6,3,4]
    s[5]=['绿','蚁','新','醅','酒','红','泥','小',\
          '火','炉','晚','来','天','欲','雪','能',\
          '饮','一','杯','无','瘦','雨','痛','氲']+['']*24
    r[5]=["绿蚁新醅酒红泥小火炉晚来天欲雪能饮一杯无",5,5,5,5]
    s[6]=['休','对','故','人','思','故','国','且',\
          '将','新','火','试','新','茶','诗','酒',\
          '趁','年','华','超','然','烟','雨','情']+['']*24
    r[6]=["休对故人思故国且将新火试新茶诗酒趁年华",7,7,5]
    s[7]=['宜','言','饮','酒','与','子','携','老',\
          '琴','瑟','在','御','莫','不','静','好',\
          '执','手','相','笙','箫','默','月','凝']+['']*24
    r[7]=["宜言饮酒与子偕老琴瑟在御莫不静好",4,4,4,4]
    s[8]=['月','落','乌','啼','霜','满','天','江',\
          '枫','渔','火','对','愁','眠','姑','苏',\
          '城','外','寒','山','寺','夜','半','钟',\
          '声','到','客','船','桥','泊','石','林']+['']*16
    r[8]=["月落乌啼霜满天江枫渔火对愁眠姑苏城外寒山寺夜半钟声到客船",7,7,7,7]
    s[9]=['昨','夜','雨','疏','风','骤','浓','睡',\
          '不','消','残','酒','试','问','卷','帘',\
          '人','却','道','海','棠','依','旧','知',\
          '西','碧','珠','醉']+['']*20
    r[9]=["昨夜雨疏风骤浓睡不消残酒试问卷帘人却道海棠依旧",6,6,5,6]
    i=randrange(10)
    return s[i],r[i]

try:
    g=catalog().click()
except GraphicsError:
    pass
