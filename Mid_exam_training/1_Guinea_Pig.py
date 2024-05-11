qty_food_kg = float(input())
qty_hay_kg = float(input())
qty_cover_kg = float(input())
weight_of_the_pig_kg = float(input())

qty_food_g = qty_food_kg * 1000
qty_hay_g = qty_hay_kg * 1000
qty_cover_g = qty_cover_kg * 1000
weight_of_the_pig_g = weight_of_the_pig_kg * 1000
qty_food_per_day = 300

for day in range(1, 31):
    qty_food_g -= qty_food_per_day
    if day % 2 == 0:
        qty_hay_g -= qty_food_g * 0.05
    if day % 3 == 0:
        qty_cover_g -= weight_of_the_pig_g / 3

if qty_food_g > 0 and qty_hay_g > 0 and qty_cover_g > 0:
    print(f"Everything is fine! Puppy is happy! Food: {qty_food_g / 1000:.2f}, Hay: {qty_hay_g / 1000:.2f}, Cover: {qty_cover_g / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")

