# def character_multiplier(data):
#     total_sum = 0
#     number = 0
#
#     if len(data[0]) > len(data[1]):
#         number = len(data[0])
#     else:
#         number = len(data[1])
#
#     for i in range(number):
#         if (len(data[0]) - 1) < i <= (len(data[1]) - 1):
#             total_sum += ord(data[1][i])
#         elif (len(data[0]) - 1) >= i > (len(data[1]) - 1):
#             total_sum += ord(data[0][i])
#         else:
#             total_sum += (ord(data[0][i]) * ord(data[1][i]))
#
#     return total_sum
#
#
# data_input = input().split()
#
# print(character_multiplier(data_input))

first_string, second_string = input().split()
total_sum = 0

if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
else:
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])

print(total_sum)
