# def caesar_cipher(text):
#     list = []
#     for letter in text:
#         new_letter = ord(letter) + 3
#         list.append(chr(new_letter))
#     return f"{''.join(list)}"
#
#
# input_text = input()
# print(caesar_cipher(input_text))

initial_message = input()
encrypted_message = ""
for character in initial_message:
    encrypted_character = chr(ord(character) + 3)
    encrypted_message += encrypted_character
print(encrypted_message)
