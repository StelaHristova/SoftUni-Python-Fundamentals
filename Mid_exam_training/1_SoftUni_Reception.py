from math import ceil, floor
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

students_per_hour = first_employee + second_employee + third_employee
# hours = ceil(students_count / students_per_hour)
# additional_hours = floor(hours / 4)
# total_hours = hours + additional_hours
# print(f"Time needed: {total_hours:.0f}h.")
hours_counter = 0
total_time = 0

while students_count > 0:
    hours_counter += 1
    total_time += 1
    if hours_counter % 4 == 0:
        continue
    students_count -= students_per_hour

print(f"Time needed: {total_time}h.")