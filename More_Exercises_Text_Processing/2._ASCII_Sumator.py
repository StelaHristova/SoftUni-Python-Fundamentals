character1 = input()
character2 = input()
random_string = input()
total_sum = 0

for character in random_string:
    if ord(character1) < ord(character) < ord(character2):
        total_sum += ord(character)

print(total_sum)
