# def data_types(input1, input2):
#     if input1 == "int":
#         print(f"{int(input2) * 2}")
#     elif input1 == "real":
#         print(f"{float(input2) * 1.5:.2f}")
#     elif input1 == "string":
#         print(f"${input2}$")
#
#
# user_input1 = input()
# user_input2 = input()
# data_types(user_input1, user_input2)

def data_types(input1, input2):
    if input1 == "int":
        return f"{int(input2) * 2}"
    elif input1 == "real":
        return f"{float(input2) * 1.5:.2f}"
    elif input1 == "string":
        return f"${input2}$"


user_input1 = input()
user_input2 = input()
print(data_types(user_input1, user_input2))