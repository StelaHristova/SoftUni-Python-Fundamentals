string_input = input()

string_input_lower = string_input.lower()

count_sand = 0
count_water = 0
count_fish = 0
count_sun = 0

if "sand" in string_input_lower:
    count_sand = string_input_lower.count("sand")
if "water" in string_input_lower:
    count_water = string_input_lower.count('water')
if "fish" in string_input_lower:
    count_fish = string_input_lower.count('fish')
if "sun" in string_input_lower:
    count_sun = string_input_lower.count('sun')
counter = count_sand + count_water + count_fish + count_sun

print(counter)
