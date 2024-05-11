def takeodd(text_input):
    new_text_input = ""
    for i in range(len(text_input)):
        if i % 2 != 0:
            new_text_input += text_input[i]
    return new_text_input


def cut(text_input, index_input, length_input):
    return text_input[0:index_input] + text_input[index_input + length_input:]


def substitute_func(text_input, old_input, new_input):
    if old_input in text_input:
        return text_input.replace(old_input, new_input), ""
    else:
        return text_input, "Nothing to replace!"


text = input()

while True:
    line = input()
    if line == "Done":
        break

    if " " not in line:
        text = takeodd(text)
        print(text)
    else:
        command_args = line.split()
        command = command_args[0]
        if command == "Cut":
            index = int(command_args[1])
            length = int(command_args[2])
            text = cut(text, index, length)
            print(text)
        elif command == "Substitute":
            substring = command_args[1]
            substitute = command_args[2]
            text, message = substitute_func(text, substring, substitute)
            if len(message) > 1:
                print(message)
            else:
                print(text)

print(f"Your password is: {text}")

