
# Car Rental Cost Calculator

# Get the number of rental days.
days = float(input("Enter the number of rental days: "))

# Get the kilometers driven.
kilometers = float(input("Enter the number of kilometers driven: "))

# Calculate the total price in dollars.
total_dollars = days + kilometers

# Convert dollars to reais.
total_reais = total_dollars * 5.49

# Show the results.
print(f"The total price in dollars is: $ {total_dollars:.2f}")
print(f"The total price in reais is: R$ {total_reais:.2f}")
