def swap(command_input, index1_input, index2_input):
    command_input[index1_input], command_input[index2_input] = command_input[index2_input], command_input[index1_input]
    return command_input


def multiply(command_input, index1_input, index2_input):
    new_input = command_input[index1_input] * command_input[index2_input]
    removed_command = command_input.pop(index1_input)
    command_input.insert(index1_input, new_input)
    return command_input


initial_array_values = [int(x) for x in input().split()]
command = input()

while command != "end":
    command_arg = command.split()
    if command_arg[0] == "swap":
        index1 = int(command_arg[1])
        index2 = int(command_arg[2])
        initial_array_values = swap(initial_array_values, index1, index2)
    elif command_arg[0] == "multiply":
        index1 = int(command_arg[1])
        index2 = int(command_arg[2])
        initial_array_values = multiply(initial_array_values, index1, index2)
    elif command_arg[0] == "decrease":
        initial_array_values = list(map(lambda x: x - 1, initial_array_values))

    command = input()
print(*initial_array_values, sep=", ")