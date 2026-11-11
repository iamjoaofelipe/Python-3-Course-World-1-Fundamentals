
# 15% Salary Increase

# Get the current salary.
salary = float(input("Enter your current salary: R$ ").replace(".", "").replace(",", "."))

# Calculate the increase.
increase = salary * 0.15

# Calculate the new salary.
new_salary = salary + increase

# Show the results.
print(f"Your current salary is: R$ {salary:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
      "and your new salary after a 15% increase is: R$",
      f"{new_salary:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
