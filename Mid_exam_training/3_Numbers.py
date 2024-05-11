#   1. Read sequence of numbers from the console
#   2. Find the average num for this sequence
#   3. Find all numbers above the average num
#   4. Sort the new collection in descending order
#   5. Check if there are numbers in the new collection
#   6. Print the top 5 numbers from the collection
FIRST_COUNT = 5

numbers = [int(x) for x in input(). split()]
avg_num = sum(numbers) / len(numbers)
filtered_nums = filter(lambda x: x > avg_num, numbers) # sorted([x for x in numbers if x > avg_num])

if not filtered_nums:
    print("No")

else:
    # for i in range(FIRST_COUNT):
    #     if filtered_nums:
    #         print(filtered_nums.pop(), end=" ")
    print(*[filtered_nums.pop() for i in range(FIRST_COUNT) if filtered_nums])