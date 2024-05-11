prices_without_tax = input()
total_price_without_taxes = 0
total_amount_of_taxes = 0
total_price_with_taxes = 0

while prices_without_tax != "special" and prices_without_tax != "regular":
    prices_without_tax = float(prices_without_tax)
    if prices_without_tax < 0:
        print("Invalid price!")
    elif prices_without_tax >= 0:
        total_price_without_taxes += prices_without_tax

    prices_without_tax = input()

total_amount_of_taxes = 0.20 * total_price_without_taxes
total_price_with_taxes = total_price_without_taxes + total_amount_of_taxes

if prices_without_tax == "special":
    total_price_with_taxes *= 0.90
if total_price_without_taxes <= 0:
    print("Invalid order!")

if total_price_without_taxes > 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_of_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")