# def emoticon_finder(text):
#     emoticons = []
#     for letter in range(len(text)):
#         if text[letter] == ":":
#             emoticon = text[letter] + text[letter + 1]
#             emoticons.append(emoticon)
#
#     return emoticons
#
#
# text_input = [str(char) for char in input()]
#
# print(*emoticon_finder(text_input), sep="\n")

single_string = input()
for index in range(len(single_string)):
    if single_string[index] == ":":
        print(f":{single_string[index + 1]}")
