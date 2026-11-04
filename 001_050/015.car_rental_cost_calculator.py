
# Calculate the car rental cost in dollars and reais.

days = float(input("Enter the number of rental days: "))
kilometers = float(input("Enter the number of kilometers driven: "))

total_dollars = days + kilometers
total_reais = total_dollars * 5.49

print(f"The total price in dollars is: $ {total_dollars:.2f}")
print(f"The total price in reais is: R$ {total_reais:.2f}")
