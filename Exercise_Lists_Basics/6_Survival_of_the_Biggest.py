list_of_integers = input().split(" ")
count_of_numbers_to_remove = int(input())
integer_list = ([int(x) for x in list_of_integers])

for number in range(count_of_numbers_to_remove):
    integer_list.remove(min(integer_list))
for i in range(len(integer_list)):
    if i == 0:
        print(integer_list[i], end ="")
    else:
        print(f", {integer_list[i]}", end="")