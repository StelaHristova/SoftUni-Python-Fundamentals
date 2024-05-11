string_name = input()

numbers_list = []
non_numbers_list = []
take_list = []
skip_list = []

for i in range(len(string_name)):
    if string_name[i].isdigit():
        numbers_list.append(int(string_name[i]))
    else:
        non_numbers_list.append(string_name[i])

for even_or_odd_index in range(len(numbers_list)):
    if even_or_odd_index % 2 == 0:
        take_list.append(numbers_list[even_or_odd_index])
    else:
        skip_list.append(numbers_list[even_or_odd_index])

take_number = 0
skip_number = 0

index = 0
final_string = ""

for a in range(len(take_list)):
    take_number = take_list[a]
    skip_number = skip_list[a]
    final_string += "".join(non_numbers_list[:take_number])
    del non_numbers_list[0:take_number+skip_number]

print(final_string)
