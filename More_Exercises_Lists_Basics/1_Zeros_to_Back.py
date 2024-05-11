single_string = input().split(", ")
integer_list = []
zeroes = 0

for element in single_string:
    integer_list.append(int(element))

for element in range(len(integer_list) - 1, -1, -1):
    if integer_list[element] == 0:
        integer_list.remove(integer_list[element])
        zeroes += 1

for zero in range(zeroes):
    integer_list.append(0)

print(integer_list)




