neighborhood_hearts = [int(x) for x in input().split("@")]
command = input()
house_index = 0

while command != "Love!":
    command = command.split()
    house_index += int(command[1])

    if house_index > (len(neighborhood_hearts) - 1):
        house_index = 0

    if neighborhood_hearts[house_index] > 2:
        neighborhood_hearts[house_index] -= 2
    elif neighborhood_hearts[house_index] == 2:
        neighborhood_hearts[house_index] -= 2
        print(f"Place {house_index} has Valentine's day.")
    elif neighborhood_hearts[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {house_index}.")
if sum(neighborhood_hearts) == 0:
    print("Mission was successful.")
else:
    house_count = 0
    for love in range(len(neighborhood_hearts)):
        if neighborhood_hearts[love] != 0:
            house_count += 1
    print(f"Cupid has failed {house_count} places.")



