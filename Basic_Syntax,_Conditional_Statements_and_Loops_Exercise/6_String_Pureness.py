number = int(input())
# characters = [",", ".", "_"]

for i in range(number):
    is_pure = True
    strings_input = input()

    for j in range(len(strings_input)):
        if strings_input[j] == "," or strings_input[j] == "." or strings_input[j] == "_":
            is_pure = False
            print(f"{strings_input} is not pure!")
            break
    if is_pure:
        print(f"{strings_input} is pure.")

    # for char in strings_input:
    #     if char in characters:
    #         is_pure = False
    #         print(f"{strings_input} is not pure!")
    #         break
    # if is_pure:
    #     print(f"{strings_input} is pure.")

    #

