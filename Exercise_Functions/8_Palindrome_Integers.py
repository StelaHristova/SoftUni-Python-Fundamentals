def check_palindrome (some_numbers):
    if some_numbers == some_numbers[::-1]:
        return True
    return False

numbers = input().split(", ")
for number in numbers:
    print(check_palindrome(number))