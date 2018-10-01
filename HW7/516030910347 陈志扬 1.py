# File:line.py
# A program to calculate the slope and intercept
# By: Daisy
def slope(p1,p2):
    x=p1[0]-p2[0]
    y=p1[1]-p2[1]
    if x==0:
        return "The line doesn't have a slope."
    else:
        k=float(y)/x
        return k
def intercept(p1,p2):
    x=p1[0]-p2[0]
    if x==0:
        return p1[0]
    else:
        k=slope(p1,p2)
        b=-k*(p1[0])+p1[1]
        return b
def main():
    p1,p2=input("Enter two points in the form of tuples divided by a comma. ")
    print "The slope of the line through the points is",slope(p1,p2)
    print "The intercept of the line through the points is",intercept(p1,p2)
main()
