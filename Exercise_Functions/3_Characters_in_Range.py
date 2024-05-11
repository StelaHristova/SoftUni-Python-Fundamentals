# character1 = input()
# character2 = input()
#
# def string_characters():
#     list_string = []
#     for i in range(ord(character1) + 1, ord(character2)):
#         list_string.append(chr(i))
#     return print(*list_string, sep=" ")
#
# string_characters()

def all_the_characters(first, second):
    characters = []
    for current_character_as_digit in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_character_as_digit))
    return characters


first_character = input()
second_character = input()
result = all_the_characters(first_character, second_character)
print(" ".join(result))