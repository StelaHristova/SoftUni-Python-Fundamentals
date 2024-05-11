def name_is_found(text):
    is_found = False
    name = ''
    for char in range(len(text)):
        if text[char] == '|':
            is_found = False
            break
        if is_found:
            name += text[char]
        if text[char] == '@':
            is_found = True
    return name

def age_is_found(text):
    age = ''
    is_found = False
    for char in range(len(text)):
        if text[char] == '*':
            is_found = False
            break
        if is_found:
            age += text[char]
        if text[char] == '#':
            is_found = True
    return age


number = int(input())

for every_num in range(number):
    line_of_strings = [str(ch) for ch in input()]

    name = name_is_found(line_of_strings)
    age = age_is_found(line_of_strings)

    print(f"{name} is {age} years old.")
