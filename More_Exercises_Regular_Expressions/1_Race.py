import re

def new_dict(dict, name, distance):
    if name not in dict:
        dict[name] = distance
    else:
        dict[name] += distance
    return dict


list_of_participants = input().split(", ")

pattern_name = r"[A-Za-z]"
pattern_digits = r"\d"

final_dict = {}

while True:
    command = input()
    name = ""
    distance = 0

    if command == "end of race":
        break

    name_list = re.findall(pattern_name, command)
    digit_list = re.findall(pattern_digits, command)

    for digit in range(len(digit_list)):
        distance += int(digit_list[digit])

    for letter in range(len(name_list)):
        name += name_list[letter]

    if name in name_list:
        final_dict = new_dict(final_dict, name, distance)

count = 0
sorted_dict = dict(sorted(final_dict.items(), key=lambda x: x[1], reverse=True))

for key in sorted_dict:
    count += 1
    if count > 3:
        exit()
    if count == 1:
        print(f"{count}st place: {key}")
    elif count == 2:
        print(f"{count}nd place: {key}")
    else:
        print(f"{count}rd place: {key}")