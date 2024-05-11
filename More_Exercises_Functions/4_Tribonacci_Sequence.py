def tribonacci_sequence(number):
    list_number = [1, 1, 2]
    for num in range(3, number):
        new_number = list_number[num - 1] + list_number[num - 2] + list_number[num - 3]
        list_number.append(new_number)
    print(*list_number)

int_number = int(input())

if int_number >= 3:
    tribonacci_sequence(int_number)
elif int_number == 2:
    list_number = [1, 1]
    print(*list_number)
elif int_number == 1:
    list_number = [1]
    print(*list_number)
