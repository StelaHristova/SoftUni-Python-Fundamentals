def results(number1, number2, number3):
    checking_list = []
    checking_list.append(number1)
    checking_list.append(number2)
    checking_list.append(number3)
    negative = 0
    for i in range(0, 3):
        if checking_list[i] < 0:
            negative += 1
        elif checking_list[i] == 0:
            print("zero")
            exit()
    if negative == 2 or negative == 0:
        print("positive")
    else:
        print("negative")

num1 = int(input())
num2 = int(input())
num3 = int(input())

results(num1, num2, num3)


#
# def results(number1, number2, number3):
#     if (number1 < 0 and number2 > 0 and number3 > 0)\
#             or (number2 < 0 and number1 > 0 and number3 > 0)\
#             or (number3 < 0 and number1 > 0 and number2 > 0):
#         return "negative"
#     elif number1 > 0 or number2 > 0 or number3 > 0:
#         return "positive"
#     elif number1 == 0 or number2 == 0 or number3 == 0:
#         return "zero"
#
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# print(results(num1, num2, num3))