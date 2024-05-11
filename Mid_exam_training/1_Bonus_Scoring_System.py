from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())

max_attendance = 0
for i in range(students):
    attendance = int(input())
    max_attendance = max(attendance, max_attendance)

total_bonus = 0
if lectures != 0:
    total_bonus = max_attendance / lectures * (5 + bonus)

print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
