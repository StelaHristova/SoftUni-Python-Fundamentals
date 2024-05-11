budget = float(input())
price_1kg_flour = float(input())
price_1pack_eggs = 0.75 * price_1kg_flour
price_1l_milk = 1.25 * price_1kg_flour
price_250ml_milk = price_1l_milk / 4
price_for_1_loaf = price_1pack_eggs + price_1kg_flour + price_250ml_milk
number_of_loaves = 0
total_price = 0
colored_eggs = 0

while budget >= total_price:
    total_price += price_for_1_loaf
    if total_price > budget:
        break
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {abs(total_price - budget - price_for_1_loaf):.2f}BGN left."
)