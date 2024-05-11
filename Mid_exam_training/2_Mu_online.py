rooms = input().split("|")
MAX_HEALTH = 100
bitcoins = 0
health = MAX_HEALTH

for index, room in enumerate(rooms, start=1):
    command, amount = room.split()
    amount = int(amount)

    if command == "potion":
        if health + amount > MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH - health} hp.")
            health = MAX_HEALTH
        else:
            print(f"You healed for {amount} hp.")
            health += amount
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        health -= amount
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {index}")
            exit(0)

print(f"You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")