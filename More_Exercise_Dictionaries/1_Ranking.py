contest_dict = {}
final_dict = {}

while True:
    current_contest = input()

    if current_contest == "end of contests":
        break

    contest_dict[current_contest] = {}

while True:
    current_username = input()

    if current_username == "end of submissions":
        break

    contest, password, username, points = current_username.split("=>")
    checking_contest = f"{contest}:{password}"
    counter = 0

    if checking_contest in contest_dict:
        for i in contest_dict[checking_contest]:
            if i == username:
                counter += 1
                if int(contest_dict[checking_contest][username]) < int(points):
                    contest_dict[checking_contest][username] = int(points)

    if (checking_contest in contest_dict) and (counter == 0):
        contest_dict[checking_contest][username] = int(points)

for ch in contest_dict.keys():
    course, result = ch.split(":")

    for key in contest_dict[ch]:
        if key not in final_dict:
            final_dict[key] = {}
            final_dict[key][course] = contest_dict[ch][key]
        else:
            final_dict[key][course] = contest_dict[ch][key]

best_candidate = ""
points = 0

for char in final_dict:
    current_points = 0
    for key in final_dict[char]:
        current_points += final_dict[char][key]

    if points < current_points:
        best_candidate = char
        points = current_points

print(f"Best candidate is {best_candidate} with total {points} points.\nRanking:")

for key, value in sorted(final_dict.items(), key=lambda x: x[0], reverse=False):
    print(key)
    for chart, digit in sorted(final_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"# {chart} -> {digit}")