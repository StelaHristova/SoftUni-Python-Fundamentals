def sorter(numbers):
    numbers_as_digit = []
    for number in numbers:
        numbers_as_digit.append(int(number))
        results = sorted(numbers_as_digit)
    return results

sequence_of_numbers_int = input().split()

print(sorter(sequence_of_numbers_int))
# sequence_of_numbers_int = [int(characher) for characher in sequence_of_numbers_int]
#
# print(sorted(sequence_of_numbers_int))



