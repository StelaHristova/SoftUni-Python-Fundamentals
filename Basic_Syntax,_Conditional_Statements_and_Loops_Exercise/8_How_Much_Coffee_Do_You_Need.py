command = input()
needed_coffee = 0

while command != "END":
    if command == "coding":
        needed_coffee += 1
    if command == "CODING":
        needed_coffee += 2
    if command == "dog" or command == "cat":
        needed_coffee += 1
    if command == "DOG" or command == "CAT":
        needed_coffee += 2
    if command == "movie":
        needed_coffee += 1
    if command == "MOVIE":
        needed_coffee += 2
    command = input()

if needed_coffee > 5:
    print("You need extra sleep")
else:
    print(needed_coffee)
