# Full Name Analyzer

# Ask the user for their full name.
name = input("Enter your full name: ").strip()

# Show the name in uppercase.
print("Your name in uppercase is:", name.upper())

# Show the name in lowercase.
print("Your name in lowercase is:", name.lower())

# Count all letters without spaces.
print("Your name has this many letters:", len(name.replace(" ", "")))

# Get the first name.
first_name = name.split()[0]

# Count the letters in the first name.
print("Your first name has this many letters:", len(first_name))