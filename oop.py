from __future__ import print_function
import math
import random

# create class 
class Circle:
    # this is constructor 
    def __init__(self , radius):
        if radius==0:
            self.radius=random.uniform(1.0, 9.5)
        else :
            self.radius=radius
    def circumreference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

# array of Object 
circles = []

for i in range(0, 10):
    c = Circle(i)

    circles.append(c)
for y in circles:
    print("The radius is : ", y.radius, " ** ", "Area is : ",
          y.area(), "Circum cerfice : ", y.circumreference())
