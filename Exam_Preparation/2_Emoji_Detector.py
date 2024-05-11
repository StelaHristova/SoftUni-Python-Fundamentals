# import re
# def cool_threshold(text_input):
#     pattern = r"[0-9]"
#     result = re.findall(pattern, text_input)
#     if result:
#         threshold = 1
#         for digit in result:
#             threshold *= int(digit)
#     return threshold
#
#
# def is_cool_emoji(text_input, threshold_sum):
#     pattern = r"[0-9]|([:]{2}[A-Z][a-z]{2,}[:]{2})|[0-9]|([*]{2}[A-Z][a-z]{2,}[*]{2})"
#     valid_emojis = re.finditer(pattern, text_input)
#     emojis_list = []
#     emoji_counter = 0
#
#     for emoji in emojis_list:
#         emoji_counter += 1
#         emoji_ascii_sum = 0
#         for letter in emoji.group():
#             if letter != ":" and letter != "*":
#                 emoji_ascii_sum += ord(letter)
#         if emoji_ascii_sum > threshold_sum:
#             emojis_list.append(emoji.group())
#
#     return emojis_list, emoji_counter
#
#
# def print_function(threshold_sum, emojis_list, count):
#     print(f"Cool threshold: {threshold_sum}")
#     print(f"{count} emojis found in the text. The cool ones are:")
#     if emojis_list:
#         for emoji in emojis_list:
#             print(f"{emoji}")
#
#
# text = input()
# threshold_sum = cool_threshold(text)
# cool_emojis, count = is_cool_emoji(text, threshold_sum)
# print_function(threshold_sum, cool_emojis, count)
#
#
#
import re


def emoji_detector():
    data = input()
    pattern = r"[0-9]|([:]{2}[A-Z][a-z]{2,}[:]{2})|[0-9]|([*]{2}[A-Z][a-z]{2,}[*]{2})"
    result = re.finditer(pattern, data)
    words = {}
    cool_threshold = 1
    for res in result:
        word = res.group()

        if word.isdigit():
            cool_threshold *= int(word)
        else:
            words[word] = 0
            for ch in word:
                if ch != ":" and ch != "*":
                    words[word] += ord(ch)

    print(f"Cool threshold: {cool_threshold}")
    print(f"{len(words)} emojis found in the text. The cool ones are:")

    for current_word in words:
        if words[current_word] >= cool_threshold:
            print(current_word)

emoji_detector()


