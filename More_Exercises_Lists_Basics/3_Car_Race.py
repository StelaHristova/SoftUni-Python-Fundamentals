sequence_of_numbers = input().split(" ")
sequence_of_time = []

for number in sequence_of_numbers:
    sequence_of_time.append(int(number))
left_car = 0
right_car = 0

for time in range((len(sequence_of_time) - 1) // 2):
    left_car += sequence_of_time[time]
    if sequence_of_time[time] == 0:
        left_car = left_car * 0.80

for time in range((len(sequence_of_time) - 1), (len(sequence_of_time) - 1) // 2, -1):
    right_car += sequence_of_time[time]
    if sequence_of_time[time] == 0:
        right_car = right_car * 0.80

if left_car > right_car:
    print(f"The winner is right with total time: {right_car:.1f}")
else:
    print(f"The winner is left with total time: {left_car:.1f}")

