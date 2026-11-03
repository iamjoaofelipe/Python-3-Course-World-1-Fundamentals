# calculate a 5% discount.

# 5% Product Discount

price = float(input("Enter the product price: R$ ").replace(".", "").replace(",", "."))

discount = price * 0.05
new_price = price - discount

print(f"The original price is: R$ {price:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
      "and the price after a 5% discount is: R$",
      f"{new_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))





