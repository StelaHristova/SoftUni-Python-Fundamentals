from audioop import reverse

number = int(input())

number_str = str(number)
sorted_number = sorted(number_str, reverse=True)
final_str = ""

for i in range(len(number_str)):
    final_str += sorted_number[i]

print(int(final_str))