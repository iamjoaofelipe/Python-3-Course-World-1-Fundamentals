# sine , cosine and tangent calculator.

# import the math functions.
from math import sin, cos, tan, radians

# get an angle in degrees.
angle = float(input("Enter an angle in degrees:"))

# convert the angle to radians.
angle = radians(angle)

# calculate sine , cosine and tangent.
sine = sin(angle) 
cosine = cos(angle)
tangent = tan(angle)

# show the results.
print("The sine of the angle is:", sine)
print("The cosine of the angle is:", cosine)    
print("The tangent of the angle is:", tangent) 
