
# Hypotenuse Calculation

# Import the hypotenuse function.
from math import hypot

# Get the opposite and adjacent sides of a right triangle.
opposite = float(input("Enter the opposite side: "))
adjacent = float(input("Enter the adjacent side: "))

# Calculate the hypotenuse.
hypotenuse = hypot(opposite, adjacent)

# Show the result.
print(f"The hypotenuse is: {hypotenuse:.2f}")
