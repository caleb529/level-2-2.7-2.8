#imports
#importing pi from Python standard library
from math import pi 

start():
  print("welcome to the caluter")
  print("choose")

#calutaions

# circle calcutation

#Getting the value of radius from user 
radius  = float(input('Enter radius of circle: '))

#Calculating the area of circle 
area = pi * radius * radius 

#Calculating the perimeter of the circle 
perimeter = 2 * radius * pi 

#Displaying the area and perimeter of cirlce to screen 
print('The area of the circle is ', area )
print('The perimeter of the circle is ', perimeter )


#rectangle
# Write a Program to find the Area of a Rectangle and 
# Perimeter of a Rectangle in Python using functions
 
def AreaOfRectangle(width, height):
 
    # calculate the area
    Area = width * height
 
    # calculate the Perimeter
    Perimeter = 2 * (width + height)
 
    print("\n Area of a Rectangle is: %.2f" %Area)
    print(" Perimeter of Rectangle is: %.2f" %Perimeter)
     
width = float(input('Please Enter the Width of a Rectangle: '))
height = float(input('Please Enter the Height of a Rectangle: '))
 
AreaOfRectangle(width, height)



#square
s=int(input("square side : "))
area=s*s
perimeter=4*s
print("Area of Rectangle : ",area)
print("Perimeter of Rectangle : ",perimeter)


#triangle
# Python Program to find the area of triangle

a = 5
b = 6
c = 7


a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)