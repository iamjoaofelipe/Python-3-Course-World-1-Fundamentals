
# Integer Part Calculator

# Get the integer part of a number.
def integer_part_calculator(number):
    return int(number)

# Get a number from the user.
number = float(input("Enter a number: "))

# Show the result.
print("The number entered is:", number,
      "and the integer part is:", integer_part_calculator(number))
