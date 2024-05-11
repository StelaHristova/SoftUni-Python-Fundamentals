# numbers_list = list(map(lambda x: round(float(x)), input().split()))
#
# print(numbers_list)




number_list = input().split()

rounded_value = []

for num in number_list:
    rounded_value.append(round(float(num)))
# rounded_value = [round(float(num)) for num in number_list]
print(rounded_value)