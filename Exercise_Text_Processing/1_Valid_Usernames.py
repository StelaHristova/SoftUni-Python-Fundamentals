# def valid_usernames(username):
#     word = []
#     valid_username = True
#     symbols = ["-", "_"]
#
#     for i in range(len(username)):
#         if 3 > len(username[i]) or len(username[i]) > 16:
#             continue
#         for letter in usernames[i]:
#             if (not letter.isalpha()) and (not letter.isdigit()) and (letter not in symbols):
#                 valid_username = False
#                 break
#
#         if valid_username:
#             word.append(username[i])
#         else:
#             valid_username = True
#     return word
#
# usernames = input().split(", ")
#
# print(*valid_usernames(usernames), sep="\n")

def length_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def characters_are_valid(username):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(username):
    if " " in username:
        return False
    return True


def username_is_valid(username):
    if length_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        return True
    return False

usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)
