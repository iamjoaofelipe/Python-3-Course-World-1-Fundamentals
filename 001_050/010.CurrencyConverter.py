
# Dollar Converter

# Get the money.
money = float(input("How much money do you have? R$: "))

# Calculate the dollars and the change.
dollars = int(money / 5.25)
change = money - (dollars * 5.25)
missing = 5.25 - change

# Show the results.
print("You can buy", dollars, "dollars.")

# Check if you can buy one dollar.
if money >= 5.25:
    print("You can buy one dollar.")
else:
    print("You need R$", missing, "more.")
5.