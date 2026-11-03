# 15% Salary Increase

salary = float(input("Enter your current salary: R$ ").replace(".", "").replace(",", "."))
increase = salary * 0.15
new_salary = salary + increase

print(f"Your current salary is: R$ {salary:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
      "and your new salary after a 15% increase is: R$", 
      f"{new_salary:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))