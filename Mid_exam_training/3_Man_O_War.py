from logging import warning


def is_valid_index(index, sequence):
    return 0 <= index < len(sequence)

pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())

is_running = True

while is_running:
    line = input()
    if line == "Retire":
        break

    command_args = line.split()
    command = command_args[0]

    if command == "Fire":
        index = int(command_args[1])
        damage = int(command_args[2])
        if not is_valid_index(index, warship):
            continue
        warship[index] -= damage
        if warship[index] <= 0:
            is_running = False
            print("You won! The enemy ship has sunken.")
    elif command == "Defend":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        damage = int(command_args[3])
        if not is_valid_index(start_index, pirate_ship) or not is_valid_index(end_index, pirate_ship):
            continue
        for index in range(start_index, end_index + 1):
            pirate_ship[index] -= damage
            if pirate_ship[index] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_running = False
                break
    elif command == "Repair":
        index = int(command_args[1])
        health = int(command_args[2])
        if not is_valid_index(index, pirate_ship):
            continue
        pirate_ship[index] = min(max_health, pirate_ship[index] + health)
    elif command == "Status":
        threshold = max_health * 0.2
        counter = 0
        for section in pirate_ship:
            if section < threshold:
                counter += 1

        print(f"{counter} sections need repair.")

if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")