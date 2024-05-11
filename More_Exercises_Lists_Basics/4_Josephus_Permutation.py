people_in_the_circle = input().split(" ")
number_k = int(input())

executed_people = []
counter = 0
index = 0

while len(people_in_the_circle) > 0:
    counter += 1
    if counter % number_k == 0:
        executed_people.append(people_in_the_circle.pop(index))
    else:
        index += 1
    if index >= len(people_in_the_circle):
        index = 0

print(str(executed_people).replace(' ', '').replace('\'', ''))