#1
import math
r=float(input("enter the radius"))
area=math.pi*r*r
print("the area of the circle is",area)



#2
filename=input("enter file name")
f=filename.split(".")
print("the extension of the file is:", f[-1])
