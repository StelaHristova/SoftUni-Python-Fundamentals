# 1. Receive initial energy
# 2. Create a variable that's keeps  track of the won battles
# 3. while we have distances or we receive end of game
#   - read distance from console
# 4. Check if distance is less than energy
#   - increase won battles with 1
#   -decrease energy with distance
#   -check if battle is third
#       -increase energy with battles count

energy = int(input())
distance = input()

battles_won = 0

while distance != "End of battle":
    distance = int(distance)

    if energy >= distance and energy > 0:
        energy -= distance
        battles_won += 1

        if battles_won % 3 == 0:
            energy += battles_won
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        break

    distance = input()

else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
