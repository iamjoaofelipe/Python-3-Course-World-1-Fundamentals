
# separating the digits of a number.

# ask the user to enter a number.
number = int(input("Enter a number from 0 to 9999: "))

# get each digit of the number.
unit = number % 10
ten = (number // 10) % 10
hundred = (number // 100) % 10
thousand = (number // 1000) % 10

# show each digit.
print(f"Unit: {unit}")
print(f"Ten: {ten}")
print(f"Hundred: {hundred}")
print(f"Thousand: {thousand}")

