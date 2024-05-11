# first_sequence = input(). split(', ')
# second_sequence = input().split(', ')
# substrings = [first_word for first_word in first_sequence\
#               if any(first_word in second_word for second_word\
#                      in second_sequence)]
#
# print(substrings)


first_sequence = input(). split(', ')
second_sequence = input().split(', ')
substrings = []

for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            substrings.append(first_string)
            break
print(substrings)
