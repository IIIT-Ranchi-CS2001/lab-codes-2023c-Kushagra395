#write a python code to find 1. area and perimeter of triangle 2.find all angles of that triangle 
from math import sqrt
a=int(input("enter the side 1 "))
b= int(input("enter the side 2 "))
c= int(input("enter the side 3 "))
s= (a+b+c)/2
area=sqrt((s*(s-a)*(s-b)*(s-c)))
print("area of triangle is " ,area ,"\n perimeter is " , a+b+c)
