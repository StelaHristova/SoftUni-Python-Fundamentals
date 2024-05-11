'''
number_of_lines = int(input())
counter_1 = 0
counter_2 = 0
for income in range(number_of_lines):
    current_input = input()
    if current_input == '(':
        counter_1 += 1
    if current_input == ')':
        counter_2 += 1
if counter_1 == counter_2:
    print('BALANCED')
else:
    print('UNBALANCED')
    '''

number_of_lines = int(input())
brackets = [None]
is_balanced = True

for line in range(number_of_lines):
    current_input = input()
    if current_input == '(' or current_input == ')':
        if current_input == brackets[-1]:
            is_balanced = False
            break
        brackets.append(current_input)
    else:
        continue
if is_balanced and brackets[1] == '(':
    print(f'BALANCED')
else:
    print(f'UNBALANCED')

