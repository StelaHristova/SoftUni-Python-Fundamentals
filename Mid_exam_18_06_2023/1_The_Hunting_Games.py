days_of_the_adventure = int(input())
number_of_players = int(input())
groups_energy = float(input())
water_per_day_for_one_person = float(input())
food_per_day_for_one_person = float(input())

total_water = days_of_the_adventure * number_of_players * water_per_day_for_one_person
total_food = days_of_the_adventure * number_of_players * food_per_day_for_one_person

for day in range(1, days_of_the_adventure + 1):
    amount_of_energy_loss = float(input())
    groups_energy -= amount_of_energy_loss

    if groups_energy <= 0:
        break

    if day % 2 == 0:
        total_water = total_water * 0.70
        groups_energy *= 1.05

    if day % 3 == 0:
        if day % 2 != 0:
            total_food -= (total_food / number_of_players)
            groups_energy *= 1.10
        else:
            total_food -= (total_food / number_of_players)
            groups_energy *= 1.10

if groups_energy > 0:
    print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")