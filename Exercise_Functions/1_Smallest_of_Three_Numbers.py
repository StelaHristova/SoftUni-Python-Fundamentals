# def smallest_number(number1, number2, number3):
#     return min(number1, number2, number3)
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print(smallest_number(num1, num2, num3))

def smallest_number(some_numbers):
    min_element = min(some_numbers)
    print(min_element)


num1 = int(input())
num2 = int(input())
num3 = int(input())
numbers = [num1, num2, num3]
smallest_number(numbers)

