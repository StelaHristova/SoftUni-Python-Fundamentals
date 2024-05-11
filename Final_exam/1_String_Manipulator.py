text = input()

while True:
    line = input()
    if line == "End":
        break

    command_args = line.split()
    command = command_args[0]

    if command == "Translate":
        char = command_args[1]
        replacement = command_args[2]
        if char in text:
            text = text.replace(char, replacement)
            print(text)
    elif command == "Includes":
        substring = command_args[1]
        if substring in text:
            print(True)
        else:
            print(False)
    elif command == "Start":
        substring = command_args[1]
        if text.startswith(substring):
            print(True)
        else:
            print(False)
    elif command == "Lowercase":
        text = text.lower()
        print(text)
    elif command == "FindIndex":
        char = command_args[1]
        counter = 0
        for letter in text[::-1]:
            if letter == char:
                finded_index = text.index(letter)
                counter = 1
                print(finded_index)
            if counter == 1:
                break

    elif command == "Remove":
        start_index = int(command_args[1])
        count = int(command_args[2])
        text = text[:start_index] + text[start_index + count:]
        print(text)


