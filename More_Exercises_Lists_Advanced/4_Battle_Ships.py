rows = int(input())
column = 0
entries = []
for row in range(rows):
    column_list = [int(number) for number in input().split(' ')]
    column = len(column_list)
    entries.append(column_list)

matrix = entries
battle_list = input().split(' ')
destroyed_ship = 0

for i in range(len(battle_list)):
    row, current_column = [int(number) for number in battle_list[i].split('-')]

    if matrix[row][current_column] > 0:
        matrix[row][current_column] -= 1
        if matrix[row][current_column] == 0:
            destroyed_ship += 1

print(destroyed_ship)

