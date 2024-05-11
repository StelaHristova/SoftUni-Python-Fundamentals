key = int(input())
number_of_lines = int(input())
message = ''

for letter in range(number_of_lines):
    current_letter = input()
    new_letter = ord(current_letter) + key
    message += chr(new_letter)

print(message)