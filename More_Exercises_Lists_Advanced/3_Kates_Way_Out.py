# def correct_maze_boundaries(row, column):
#     if row < 0 or column < 0 or row >= len(input_list) or column >= len(input_list[0]):
#         return True
#
#
# def wall_check(row, column):
#     if input_list[row][column] in "#v":
#         return True
#
#
# def find_exit(row, column):
#     if row == 0 or column == len(input_list) - 1 or column == 0 or column == len(input_list[0]):
#         return True
#
#
# def find_start_point():
#     for position_row, row in enumerate(input_list):
#         for position_column, column in enumerate(row):
#             if column == "k":
#                 return position_row, position_column
#
#
# def find_the_path(row, column, path):
#     if correct_maze_boundaries(row, column) or wall_check(row, column):
#         return
#
#     steps.append(1)
#
#     if find_exit(row, column):
#         max_len_path.append(sum(steps))
#
#     path[row][column] = "v"
#     find_the_path(row, column + 1, path) #check right
#     find_the_path(row, column - 1, path) #check left
#     find_the_path(row + 1, column, path) #check up
#     find_the_path(row - 1, column, path) #check down
#     path[row][column] = ""
#
#     steps.pop()
#
# rows = int(input())
# input_list = []
# steps = []
# max_len_path = []
#
# for i in range(rows):
#     input_list.append(list(input()))
#
# columns = len(input_list[0])
# start_row, start_column = find_start_point()
#
# find_the_path(start_row, start_column, input_list)
#
# if max_len_path:
#     print(f"Kate got out in {max(max_len_path)} moves")
# else:
#     print("Kate cannot get out")

def correct_lab_bounds(row, column):
    if row < 0 or column < 0 or row >= len(input_list) or column >= len(input_list[0]):
        return True


def check_wall(row, column):
    if input_list[row][column] in "#v":
        return True


def find_exit(row, column):
    if row == 0 or row == len(input_list) - 1 or column == 0 or column == len(input_list[0]):
        return True


def find_starting_point():
    for position_row, row in enumerate(input_list):
        for position_column, column in enumerate(row):
            if column == "k":
                return position_row, position_column


def find_the_lab_path(row, column, path):
    if correct_lab_bounds(row, column) or check_wall(row, column):
        return

    steps.append(1)

    if find_exit(row, column):
        max_len_path.append(sum(steps))

    path[row][column] = "v"
    find_the_lab_path(row, column + 1, path)  # check right
    find_the_lab_path(row, column - 1, path)  # check left
    find_the_lab_path(row + 1, column, path)  # check up
    find_the_lab_path(row - 1, column, path)  # check down
    path[row][column] = " "

    steps.pop()


rows = int(input())
input_list = []
steps = []
max_len_path = []
for curr_lab in range(rows):
    input_list.append(list(input()))
cols = len(input_list[0])
start_row, start_col = find_starting_point()

find_the_lab_path(start_row, start_col, input_list)

if max_len_path:
    print(f"Kate got out in {max(max_len_path)} moves")
else:
    print("Kate cannot get out")