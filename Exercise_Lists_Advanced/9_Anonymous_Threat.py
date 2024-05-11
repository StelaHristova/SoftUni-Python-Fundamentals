def merge(list, start_index, end_index):
    if start_index < 0:
        start_index = 0
    if end_index > len(list) - 1:
        end_index = len(list) - 1
    for index, string in enumerate(list):
        if index in range(start_index + 1, end_index + 1):
            list[start_index] += list[index]
    for i in range(end_index, start_index, -1):
        list.pop(i)
    return list


def divide(list, index, partitions):
    if partitions > len(list[index]):
        step = 1
    else:
        step = len(list[index]) // partitions
    divided_part = list.pop(index)
    start = 0
    for parts in range(partitions):
        if parts == partitions - 1:
            list.insert(index, divided_part[start::])
            break
        else:
            list.insert(index, divided_part[start: start + step:])
        start += step
        index += 1


input_list = [i for i in input().split(" ")]

while True:
    current_string = input()

    if current_string == "3:1":
        break

    current_string_list = current_string.split(" ")

    if current_string_list[0] == "merge":
        start_index = int(current_string_list[1])
        end_index = int(current_string_list[2])
        input_list = merge(input_list, start_index, end_index)
    elif current_string_list[0] == "divide":
        index = int(current_string_list[1])
        partitions = int(current_string_list[2])
        divide(input_list, index, partitions)

print(" ".join(input_list))
