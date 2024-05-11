sequence_of_integers = [int(number) for number in input().split()]
summed_value = 0

while len(sequence_of_integers) > 0:
    indexes = int(input())

    current_number = 0

    if indexes > len(sequence_of_integers) - 1:
        indexes = len(sequence_of_integers) - 1
        current_number += sequence_of_integers[indexes]
        del sequence_of_integers[indexes]
        sequence_of_integers.append(sequence_of_integers[0])

    elif indexes < 0:
        indexes = 0
        current_number += sequence_of_integers[0]
        del sequence_of_integers[0]
        sequence_of_integers.insert(0, sequence_of_integers[-1])

    else:
        current_number += sequence_of_integers[indexes]
        del sequence_of_integers[indexes]

    for i in range(0, len(sequence_of_integers)):
        if sequence_of_integers[i] > current_number:
            sequence_of_integers[i] -= current_number
        elif sequence_of_integers[i] <= current_number:
            sequence_of_integers[i] += current_number

    summed_value += current_number

print(summed_value)

