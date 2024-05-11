username_max_points = {}
language_number = {}
while True:
    line = input()
    if line == "exam finished":
        break
    args = line.split("-")
    if len(args) == 3:
        username = args[0]
        language = args[1]
        points = int(args[2])

        if username not in username_max_points.keys():
            username_max_points[username] = 0
        if username_max_points[username] < points:
            username_max_points[username] = points
        if language not in language_number.keys():
            language_number[language] = 0
        language_number[language] += 1

    else:
        if args[0] in username_max_points:
            del username_max_points[args[0]]

print("Results:")
for key, values in username_max_points.items():
    print(f"{key} | {values}")
print("Submissions:")
for key, values in language_number.items():
    print(f"{key} - {values}")




