single_string = input()

final_list = []

for i in range(len(single_string)):
    current_letter = single_string[i]
    if 65 <= ord(current_letter) <= 90:
        final_list.append(i)

print(final_list)