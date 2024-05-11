# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
#
#
# def sum_numbers():
#     return number1 + number2
#
# def subtract():
#     return sum_numbers() - number3
#
#
# print(subtract())

def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def add_and_subtract(number_one, number_two, number_three):
    sum_of_first_and_second_numbers = sum_numbers(number_one, number_two)
    result = subtract(sum_of_first_and_second_numbers, number_three)
    return result

first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
