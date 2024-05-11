import sys
line_of_integers = [int(integer) for integer in input().split(" ")]
command = input().split()
final_list = []
while command[0] != "end":
    even_numbers = [even for even in line_of_integers if even % 2 == 0]
    odd_numbers = [odd for odd in line_of_integers if odd % 2 != 0]
    max_value = -sys.maxsize
    min_value = sys.maxsize
    index_value = 0
    is_found = False
    counter = 0

    if command[0] == "exchange":
        ex_index = int(command[1])
        new_list = []
        if ex_index < 0 or ex_index >= len(line_of_integers):
            print("Invalid index")
        else:
            for index in range(ex_index + 1, len(line_of_integers)):
                new_list.append(line_of_integers[index])
            for index in range(0, ex_index + 1):
                new_list.append(line_of_integers[index])
            line_of_integers = new_list

    elif command[0] == "max":
        if command[1] == "even":
            for index, value in enumerate(line_of_integers):
                if value % 2 == 0:
                    if value >= max_value:
                        max_value = value
                        index_value = index
                        is_found = True
        elif command[1] == "odd":
            for index, value in enumerate(line_of_integers):
                if value % 2 != 0:
                    if value >= max_value:
                        max_value = value
                        index_value = index
                        is_found = True
        if is_found:
            print(index_value)
        else:
            print("No matches")

    elif command[0] == "min":
        if command[1] == "even":
            for index, value in enumerate(line_of_integers):
                if value % 2 == 0:
                    if value <= min_value:
                        min_value = value
                        index_value = index
                        is_found = True
        elif command[1] == "odd":
            for index, value in enumerate(line_of_integers):
                if value % 2 != 0:
                    if value <= min_value:
                        min_value = value
                        index_value = index
                        is_found = True
        if is_found:
            print(index_value)
        else:
            print("No matches")

    elif command[0] == "first":
        counter = int(command[1])
        if command[2] == "even":
            if counter > len(line_of_integers):
                print("Invalid count")
            else:
                print(even_numbers[:counter])
        elif command[2] == "odd":
            if counter > len(line_of_integers):
                print("Invalid count")
            else:
                print(odd_numbers[:counter])

    elif command[0] == "last":
        counter = int(command[1])
        if command[2] == "even":
            if counter > len(line_of_integers):
                print("Invalid count")
            else:
                print(even_numbers[-counter:])
        elif command[2] == "odd":
            if counter > len(line_of_integers):
                print("Invalid count")
            else:
                print(odd_numbers[-counter:])

    command = input().split()

print(line_of_integers)
