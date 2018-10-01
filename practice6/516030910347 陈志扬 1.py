#File: sphere.py
#A class to represent the geometric solid sphere
# By: Daisy
from math import pi
class sphere:
    def __init__(self,radius):
        self.r=radius
    def surface(self):
        self.s=4*pi*(self.r)**2
        return self.s
    def volume(self):
        self.v=4/3*pi*(self.r)**3
        return self.v
def main():
    radius=input("Enter the radius of the sphere. ")
    s=sphere(radius).surface()
    v=sphere(radius).volume()
    print "The surface of the sphere is",s
    print "The volume of the sphere is",v

main()
