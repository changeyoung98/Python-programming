# futval_graph.py
# A program to compute the value of an investment carried 10 years into the future
# By:Daisy
from graphics import *
def main():
    # Introduction print "This program plots the growth of a 10 year investment."
    # Get principal and interest rate
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(90,70),'principal').draw(win)
    Text(Point(100,90),'apr').draw(win)
    input1=Entry(Point(160,70),8)
    input1.draw(win)
    input2=Entry(Point(160,90),5)
    input2.draw(win)
    win.getMouse()
    principal = eval(input1.getText())
    apr = eval(input2.getText())
    # Create a graphics window with labels on left edge
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5k').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)
    # Draw bar of initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    # Draw bars for successive years
    for year in range(1,11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    Text(Point(240,10),'Click  to quit.').draw(win)
    win.getMouse()
    win.close()
main()
