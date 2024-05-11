sequence_of_numbers = input().split(" ")
string = input()
string = list(string)
final_message = []

for number in sequence_of_numbers:
    current_number = list(number)
    index = -len(string)

    for char in current_number:
        digit = int(char)
        index += digit

    final_message.append(string[index])
    string.remove(string[index])

print("".join(final_message))
