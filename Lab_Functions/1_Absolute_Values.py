number_list = input().split()

absolute_value = []

for num in number_list:
    absolute_value.append(abs(float(num)))
# absolute_value = [abs(float(num)) for num in number_list]
print(absolute_value)