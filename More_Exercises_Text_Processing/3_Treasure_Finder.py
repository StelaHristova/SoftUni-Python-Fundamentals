def looping_through_text(list, code):
    code_counter = -1
    looping_text = ''

    for char in range(len(list)):
        code_counter += 1
        looping_text += chr(ord(list[char]) - int(code[code_counter]))
        if len(code) - 1 == code_counter:
            code_counter = -1
    return looping_text


def treasure_finding(list):
    type_counter = 0
    coordinates_counter = 0
    type = ''
    coordinates = ''
    for char in list:
        if char == '&':
            type_counter += 1
        if char == '<' or char == '>':
            coordinates_counter += 1
        if 0 < type_counter < 2:
            type += char
        if 0 < coordinates_counter < 2:
            coordinates += char

    return type[1::], coordinates[1::]

key = [int(ch) for ch in input().split()]

while True:
    message = input()
    if message == 'find':
        break

    message_list = [str(ch) for ch in message]
    new_message = [str(ch) for ch in looping_through_text(message_list, key)]

    type, coordinates = treasure_finding(new_message)

    print(f"Found {type} at {coordinates}")