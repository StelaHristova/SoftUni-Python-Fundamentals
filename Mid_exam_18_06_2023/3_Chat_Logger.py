def chat(input_list, message_input):
    input_list.append(message_input)
    return input_list


def delete(input_list, message_input):
    if message_input in input_list:
        input_list.remove(message_input)
    return input_list


def edit(input_list, message_input, edited_version_input):
    if message_input in input_list:
        index_message_input = input_list.index(message_input)
        input_list[index_message_input] = edited_version_input
        # input_list.replace(message_input, edited_version_input)
    return input_list


def pin(input_list, message_input):
    if message_input in input_list:
        input_list.remove(message_input)
        input_list.append(message_input)
    return input_list


def spam(input_list, message_list):
    input_list.extend(message_list)
    return input_list


command_list = input(). split()
command = command_list[0]
new_list = []

while command != "end":
    if command == "Chat":
        message = command_list[1]
        new_list = chat(new_list, message)
    elif command == "Delete":
        message = command_list[1]
        new_list = delete(new_list, message)
    elif command == "Edit":
        message = command_list[1]
        edited_version = command_list[2]
        new_list = edit(new_list, message, edited_version)
    elif command == "Pin":
        message = command_list[1]
        new_list = pin(new_list, message)
    elif command == "Spam":
        messages_list = command_list[1:]
        new_list = spam(new_list, messages_list)

    command_list = input().split()
    command = command_list[0]

print(*new_list, sep="\n")