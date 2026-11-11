
# Product Discount Calculator

# Get the product price.
price = float(input("Enter the product price: R$ ").replace(".", "").replace(",", "."))

# Calculate the discount.
discount = price * 0.05

# Calculate the new price.
new_price = price - discount

# Show the results.
print(f"The original price is: R$ {price:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
      "and the price after a 5% discount is: R$",
      f"{new_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
