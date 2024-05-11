
names_of_gifts = input().split(" ")
# 1 Solution
# commands = input().split()

# while "Money" not in commands:
#
#     if "OutOfStock" in commands:
#         for element in range(len(names_of_gifts)):
#             if commands[1] in names_of_gifts[element]:
#                 names_of_gifts[element] = "None"
#     elif "Required" in commands:
#         for element in range(len(names_of_gifts)):
#             if element == int(commands[2]):
#                 names_of_gifts[element] = commands[1]
#     elif "JustInCase" in commands:
#         names_of_gifts[-1] = commands[1]
#     commands = input().split()
#
# while "None" in names_of_gifts:
#     names_of_gifts.remove("None")
# for element in names_of_gifts:
#     print(element, end=" ")
#
# 2 Solution
command = input()
while command != "No Money":
    command_list = command.split(" ")
    command = command_list[0]
    gift = command_list[1]
    index = command_list[-1]

    if (gift != index) and (0 <= int(index) < len(names_of_gifts)):
        index_is_valid = True
    else:
        index_is_valid = False

    if command == "OutOfStock":
        for i in range(len(names_of_gifts)):
            if names_of_gifts[i] == gift:
                names_of_gifts[i] = "None"
    elif command == "Required":
        if index_is_valid:
            names_of_gifts[int(index)] = gift
    elif command == "JustInCase":
        names_of_gifts[-1] = gift
    command = input()

for element in range(len(names_of_gifts)):
    if names_of_gifts[element] != "None":
        print(names_of_gifts[element], end=" ")