# word = input()
# output = []
# current_ch = ""
#
# for digit in word:
#     if digit != current_ch:
#         current_ch = digit
#         output.append(current_ch)
#
# print(''.join(output))

text = input()
final_text = ""
last_character = ""
for current_character in text:
    if current_character != last_character:
        final_text += current_character
        last_character = current_character
print(final_text)