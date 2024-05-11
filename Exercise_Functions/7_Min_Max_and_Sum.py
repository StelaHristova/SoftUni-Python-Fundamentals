def output(numbers):
    list_of_numbers = []
    for number in numbers:
        list_of_numbers.append(int(number))
    print(f"The minimum number is {min(list_of_numbers)}")
    print(f"The maximum number is {max(list_of_numbers)}")
    print(f"The sum number is: {sum(list_of_numbers)}")


sequence_of_numbers = input().split(" ")
output(sequence_of_numbers)