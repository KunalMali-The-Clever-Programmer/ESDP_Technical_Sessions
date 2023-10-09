#Q.Menu Driven Program
''' import sys
import math
def addition():
  n1=int(input("Enter n1 value:"))
  n2=int(input("Enter n2 value:"))
  res=n1+n2
  print("Addition = ",res)

def subtraction():
  n1=int(input("Enter n1 value:"))
  n2=int(input("Enter n2 value:"))
  res=n1-n2
  print("Subtraction = ",res)

def multiplication():
  n1=int(input("Enter n1 value:"))
  n2=int(input("Enter n2 value:"))
  res=n1*n2
  print("Multiplication = ",res)

def division():
  n1=int(input("Enter n1 value:"))
  n2=int(input("Enter n2 value:"))
  res=n1/n2
  print("Division = ",res)

def areaofcircle():
  r=float(input("Enter the Radius = "))
  area=math.pi*r**2
  print("Area of Circle is = ",area)

def areaofrectangle():
    l=int(input("Enter the length ="))
    b=int(input("Enter the breadth ="))
    area=l*b
    print("Area of Rectangle = ",area) 
def volumeofsphere():
  r=float(input("Enter the Radius = "))
  volume=4/3*math.pi*r**3
  print("Volume of Sphere = ",volume)

def surfaceareaofsphere():
  r=float(input("Enter the Radius = "))
  surface=4*math.pi*r**2
  print("Surface area of sphere",surface)

while True:
  print("\n\n1.Addition = ")
  print("\n\n2.subtraction = ")
  print("\n\n3.Multiplication = ")
  print("\n\n4.Division = ")
  print("\n\n5.Area of circle = ")
  print("\n\n6.Area of Rectangle = ")
  print("\n\n7.Volume of Shere = ")
  print("\n\n8.Surface area of Shere = ")
  print("\n\n0.Exit = ")
  ch=int(input("\n\nSelect any choice = "))
  if ch==1:
    addition()
  elif ch==2:
    subtraction()
  elif ch==3:
    multiplication()
  elif ch==4:
    division()
  elif ch==5:
    areaofcircle()
  elif ch==6:
    areaofrectangle()
  elif ch==7:
    areaofrectangle()
  elif ch==8:
    surfaceareaofsphere()
  elif ch==0:
    sys.exit()
  else:
    print("Invalid input")'''



#vaiables

''' def add(a,b):
    return a+b
s=lambda a,b:a+b
print(add(11,22))'''

#Example

''' s=lambda a,b:a+b
print(s(2,3))
print(s(11,22))

s=lambda a,b:a-b
print(s(4,5))
print(s(11,22))

s=lambda a,b:a*b
print(s(10,37))
print(s(11,22))

s=lambda a,b:a/b
print(s(35,7))
print(s(11,22))''' 

#Module
''' import rcpit
a=int(input("Enter a value = "))
b=int(input("Enter b value = "))
rcpit.add(a,b)'''

#from import
''' from rcpit import add
a=int(input("Enter a value = "))
b=int(input("Enter b value = "))
add(a,b)''' 

#pakages
''' from sanika.rcpit import add
a=int(input("Enter a value = "))
b=int(input("Enter b value = "))
sanika.rcpit.add(a,b)'''

f=open("myfile.txt",'w')
f.write("Sanika\n")
f.write("Ashwini\n")
f.write("Divya\n")
print("write operation done successfuly")
f.colse()














