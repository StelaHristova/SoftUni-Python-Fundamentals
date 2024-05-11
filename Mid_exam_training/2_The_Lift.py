#   1.Read people count from the console
#   2. Read cabins current state from the console
#   3. Iterate over every cabin and put as much people as possible in it(MAX4)
#       -find free spaces in cabin(MAX size - current state of cabin = free spaces)
#       -fill the cabin
#       - decrease number of waiting people
#       -check if there are no more people of cabins
MAX_SIZE = 4

people = int(input())
lift = [int(x) for x in input().split()]

for i in range(len(lift)):
    free_spaces = MAX_SIZE - lift[i]

    if people >= free_spaces:
        lift[i] += free_spaces
    else:
        lift[i] += people

    people -= free_spaces

    if people <= 0 and (i != len(lift) - 1 or lift[i] < MAX_SIZE):
        print(f"The lift has empty spots!")
        break
else:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")

print(*lift)

