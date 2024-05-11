# def rate(dict, plant, rating):
#     for char in dict:
#         if char == plant:
#             for key in dict[char]:
#                 dict[char][key].append(int(rating))
#     return dict
#
#
# def update(dict, plant, rarity):
#     for char in dict:
#         if char == plant:
#             list = []
#             for key in dict[char]:
#                 list = dict[char][key]
#                 dict[char] = {}
#                 dict[char][rarity] = list
#     return dict
#
#
# def reset(dict, plant):
#     for char in dict:
#         if char == plant:
#             for key in dict[char]:
#                 dict[char][key] =[]
#     return dict
#
# n = int(input())
# plant_name = {}
#
# for i in range(n):
#     plant_arg = input().split("<->")
#     plant = plant_arg[0]
#     rarity = int(plant_arg[1])
#     plant_name[plant] = {}
#     plant_name[plant][rarity] = []
#
# while True:
#     line = input()
#     if line == "Exhibition":
#         break
#
#     command_arg = line.split(": ")
#     command = command_arg[0]
#     next_command = command_arg[1]
#
#     if command == "Rate":
#         current_plant_rating = next_command.split(" - ")
#         plant = current_plant_rating[0]
#         rating = int(current_plant_rating[1])
#         if plant in plant_name:
#             plant_name = rate(plant_name, plant, rating)
#         else:
#             print("error")
#
#     elif command == "Update":
#         plant, new_rarity = next_command.split(" - ")
#         if plant in plant_name:
#             plant_name = update(plant_name, plant, new_rarity)
#         else:
#             print("error")
#
#     elif command == "Reset":
#         plant = next_command
#         if plant in plant_name:
#             plant_name = reset(plant_name, plant)
#         else:
#             print("error")
#
# print("Plants for the exhibition:")
# for i in plant_name:
#     plant_name_in_dict = i
#     rarity = ""
#     average_rating = 0
#     for char in plant_name[i]:
#         rarity = char
#         if len(plant_name[i][char]) > 0:
#             average_rating = (sum(plant_name[i][char]) / len(plant_name[i][char]))
#     print(f"- {plant_name_in_dict}; Rarity: {rarity}; Rating: {average_rating:.2f}")
def create_plants_data(plants, number):
    for _ in range(number):
        data = input().split("<->")
        name_of_plant = data[0]
        rarity = int(data[1])

        if name_of_plant not in plants:
            plants[name_of_plant] = {'rarity': rarity, 'rating': []}
        else:
            plants[name_of_plant]['rarity'] = rarity
    return plants


def additional_plants_data(plants):

    while True:
        command = input().split(': ')

        if command[0] == "Exhibition":
            break

        data = command[1].split(' - ')
        type_of_command = command[0]
        plant = data[0]

        if plant not in plants:
            print('error')
            continue

        if type_of_command == "Rate":
            rating = int(data[1])
            plants[plant]['rating'].append(rating)

        elif type_of_command == "Update":
            new_rarity = int(data[1])
            plants[plant]['rarity'] = new_rarity

        elif type_of_command == "Reset":
            plants[plant]['rating'].clear()

    return plants

def print_function(plants):
    print("Plants for the exhibition:")

    for dict_el in plants:
        if len(plants[dict_el]['rating']) > 0 and sum(plants[dict_el]['rating']) > 0:
            average_rating = sum(plants[dict_el]['rating']) / len(plants[dict_el]['rating'])
        else:
            average_rating = 0
        rarity = plants[dict_el]['rarity']
        print(f"- {dict_el}; Rarity: {rarity}; Rating: {average_rating:.2f}")

def plant_discovery(number):
    plants = {}

    create_plants_data(plants, number)
    additional_plants_data(plants)
    print_function(plants)


n = int(input())
plant_discovery(n)