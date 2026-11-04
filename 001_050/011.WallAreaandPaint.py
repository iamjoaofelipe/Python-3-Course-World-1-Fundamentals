# Calculate the wall area and paint amount.

import math

width = (float(input("wall width in meters:" ))) 
height = (float(input("wall height in meters:" )))

area = width * height
paint = math.ceil(area / 2)

print("Wall area:", area, "square meters")
print("paint needed:", paint, "liters")  

