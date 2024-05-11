# def string_explosion(text):
#     output_list = []
#     explosion = 0
#
#     for ch in range(len(text)):
#         if not text[ch] == ">" and explosion > 0:
#             explosion -= 1
#         elif text[ch] == ">":
#             explosion += int(text[ch + 1])
#             output_list += text[ch]
#         else:
#             output_list += text[ch]
#
#     return output_list
#
#
# text_input = input()
#
# print(''.join(string_explosion(text_input)))
some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    elif some_string[index] == ">":
        final_string += some_string[index]
        strength += int(some_string[index + 1])
    else:
        final_string += some_string[index]
print(final_string)