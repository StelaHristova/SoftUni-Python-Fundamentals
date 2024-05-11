'''
n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

command = input()
filtered_numbers = []

if command == 'even':
    for num in numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)

elif command == 'odd':
    for num in numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)

elif command == 'negative':
    for num in numbers:
        if num < 0:
            filtered_numbers.append(num)

elif command == 'positive':
    for num in numbers:
        if num >= 0:
            filtered_numbers.append(num)

print(filtered_numbers)'''

n = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'

numbers = [int(input()) for i_ in range(n)]

filtered_numbers = []

command = input()

for num in numbers:
    filtered_command = ((command == COMMAND_EVEN and num % 2 == 0) or \
                        (command == COMMAND_ODD and num % 2 != 0) or\
                        (command == COMMAND_POSITIVE and num >= 0) or\
                        (command == COMMAND_NEGATIVE and num < 0))

    if filtered_command:
        filtered_numbers.append(num)

print(filtered_numbers)

'''
n = int(input())

positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []

for i in range(n):
    current_number = int(input())
    
    if current_number >= 0:
        positive_nums.append(current_number)
    else:
        negative_nums.append(current_number)
    
    if current_number % 2 == 0:
        even_nums.append(current_number)
    else:
        odd_nums.append(current_number)
        
command = input()

if command == 'even':
    print(even_nums)
elif command == 'odd':
    print(odd_nums)
elif command == 'positive':
    print(positive_nums)
elif command == 'negative':
    print(negative_nums)
    
'''