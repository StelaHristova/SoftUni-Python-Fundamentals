def include(command_list, coffee):
    command_list.append(coffee)
    return command_list


def remove(command_list, position_in_list, count_coffees):
    if int(count_coffees) in range(len(command_list)):
        if position_in_list == "first":
            command_list = command_list[int(count_coffees):]
        elif position_in_list == "last":
            command_list = command_list[:-int(count_coffees)]
    return command_list


def prefer(command_list, coffee_index1, coffee_index2):
    if int(coffee_index1) < len(command_list) and int(coffee_index2) < len(command_list):
        command_list[int(coffee_index1)], command_list[int(coffee_index2)] = command_list[int(coffee_index2)], command_list[int(coffee_index1)]
    return command_list


def reverse(command_list):
    command_list.reverse()
    return command_list


coffee_list = input().split()
count_command = int(input())

for counter in range(count_command):
    command_line = input().split()
    command = command_line[0]

    if command == "Include":
        coffee = command_line[1]
        coffee_list = include(coffee_list, coffee)
    elif command == "Remove":
        position = command_line[1]
        numbers_of_coffee = int(command_line[2])
        coffee_list = remove(coffee_list, position, numbers_of_coffee)
    elif command == "Prefer":
        index1 = int(command_line[1])
        index2 = int(command_line[2])
        coffee_list = prefer(coffee_list, index1, index2)
    elif command == "Reverse":
        coffee_list = reverse(coffee_list)

print("Coffees:")
print(" ".join(coffee_list))
