courses = {}
args = input().split(" : ")
while args[0] != "end":

    course_name = args[0]
    student_name = args[1]

    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student_name)
    args = input().split(" : ")
for course_name, students in courses.items():
    print(f"{course_name}: {len(students)}")

    for student in students:
        print(f"-- {student}")