'''for i in range(n):
    for j in range(n - i):
        print(end= '')
    for j in range(i + 1):
        print('*', end= '')
    print()'''

'''for i in range(n - 1, 0, -1):
    for j in range(n - i + 1):
        print(end= '')
    for j in range(i):
        print('*', end= '')
    print()'''


'''def heart_pattern():
    for y in range(20, -20, -1):
        current_resource = ''
        for x in range(-30, 30):
            if (((x * 0.04) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.04) ** 2 * (y * 0.1) ** 3) <= 0:
               current_resource += '*'
            else:
                current_resource +=''
        print(current_resource)

heart_pattern()'''