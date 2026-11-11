
# Wall Area and Paint Calculator

# Import the ceil function.
from math import ceil

# Get the wall width.
width = float(input("Enter the wall width in meters: "))

# Get the wall height.
height = float(input("Enter the wall height in meters: "))

# Find the wall area.
area = width * height

# Find the paint amount.
paint = ceil(area / 2)

# Show the results.
print("Wall area:", area, "square meters")
print("Paint needed:", paint, "liters")
