# separating the digits of a number.

# ask the user to enter a number.
number = int(input("Enter a number from 0 to 9999:"))

# get each digit of the number.
unit = number % 10
ten = (number // 10) % 10
hundred = (number // 100) % 10
thousand = (number // 1000) % 10

# show each digit.
print(f"unit: {unit}")
print(f"ten: {ten}")
print(f"hundred: {hundred}")
print(f"thousand: {thousand}")

