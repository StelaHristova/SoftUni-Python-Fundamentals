n = int(input())

for i in range(1, n + 1):
    num = str(i)
    is_special = False
    sum_of_digits = 0
    for character in num:
        sum_of_digits += int(character)
    if sum_of_digits in [5, 7, 11]:
        is_special = True
    print(f'{i} -> {is_special}')
