from __future__ import print_function
import math


# super class 
class shape:
    def __init__(self):
        self.color="red"
        self.shides=5
    def calcArea(self):
        return 0


# sub1 class 
class rec(shape):
    def __init__(self , w , c):
        shape.__init__(self)
        self.width=w
        self.color=c

    def calcArea(self):
        return self.width**2
# sub2 class 
class circle(shape):
    def __init__(self , r ):
        shape.__init__(self)
        self.radius=r
    def calcArea(self):
        return math.pi*(self.radius**2)
    
       


# create objects from these classes 
rec1=rec(50 ,"blue")
rec2=rec(30 , "yello")
circle1=circle(.5)

# print functions 
print("Square : ", rec1.width , "    " , rec2.width ,"\n" ,rec1.color , "   " , rec2.color , "Area is : ", rec1.calcArea() , end="\n")
print("Circle : ", circle1.color ,"    ", circle1.shides , "Area is : ", circle1.calcArea())










