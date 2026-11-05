# double , triple and square root.

# import the math funcions.
from math import sqrt,prod,ceil

# get a number.
number = float(input("Enter a number: "))

# get the double of the number.
double = prod([ceil(number),2]) 

# get the triple of the number.
triple = prod([ceil(number),3]) 

# get the square root of the number.
square_root = sqrt(ceil(number))

# show the results.

# show the number entered.
print("The number entered is:", number)

# show the double of the number.
print("The double of the number is:", double)

# show the triple of the number.
print("The triple of the number is:", triple)

# show the square root of the number.
print("The square root of the number is:", ceil(square_root)) 

