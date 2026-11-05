# Value Analyzer

# Ask the user for a value.
value = input("Enter a value: ")

# Show the value type.
print("Value type:", type(value))

# Check if the value has only spaces.
print("Only spaces?", value.isspace())

# Check if the value has only numbers.
print("Is a number?", value.isnumeric())

# Check if the value has only uppercase letters.
print("Is uppercase?", value.isupper())

# Check if the value has only lowercase letters.
print("Is lowercase?", value.islower())

# Check if the value has title case.
print("Is title case?", value.istitle())