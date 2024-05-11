#
# capacity_of_possible_messages = int(input())
# mail_dict = {}
#
# while True:
#     line = input()
#     if line == "Statistics":
#         break
#
#     command_args = line.split("=")
#     command = command_args[0]
#
#     if command == "Add":
#         username = command_args[1]
#         sent = int(command_args[2])
#         received = int(command_args[3])
#
#         if username not in mail_dict:
#             mail_dict[username] = [sent, received]
#             if sum(mail_dict[username]) >= capacity_of_possible_messages:
#                 print(f"{username} reached the capacity!")
#                 del mail_dict[username]
#
#     elif command == "Message":
#         sender = command_args[1]
#         receiver = command_args[2]
#
#         if sender in mail_dict and receiver in mail_dict:
#             mail_dict[sender][0] += 1
#             mail_dict[receiver][1] += 1
#             if sum(mail_dict[sender]) >= capacity_of_possible_messages:
#                 print(f"{sender} reached the capacity!")
#                 del mail_dict[sender]
#             if sum(mail_dict[receiver]) >= capacity_of_possible_messages:
#                 print(f"{receiver} reached the capacity!")
#                 del mail_dict[receiver]
#
#     elif command == "Empty":
#         username = command_args[1]
#         if username == "All":
#             mail_dict.clear()
#         else:
#             if username in mail_dict:
#                 del mail_dict[username]
#
# print(f"Users count: {len(mail_dict)}")
# for username in mail_dict:
#     print(f"{username} - {sum(mail_dict[username])}")
#

def add(username, sent, received):
    if username not in mail_dict:
        mail_dict[username] = [sent, received]
        if sum(mail_dict[username]) >= capacity_of_possible_messages:
            print(f"{username} reached the capacity!")
            del mail_dict[username]

def message(sender, receiver):
    if sender in mail_dict and receiver in mail_dict:
        mail_dict[sender][0] += 1
        mail_dict[receiver][1] += 1
        if sum(mail_dict[sender]) >= capacity_of_possible_messages:
            print(f"{sender} reached the capacity!")
            del mail_dict[sender]
        if sum(mail_dict[receiver]) >= capacity_of_possible_messages:
            print(f"{receiver} reached the capacity!")
            del mail_dict[receiver]

def empty(username):
    if username == "All":
        mail_dict.clear()
    else:
        if username in mail_dict:
            del mail_dict[username]

capacity_of_possible_messages = int(input())
mail_dict = {}

while True:
    line = input()
    if line == "Statistics":
        break

    command_args = line.split("=")
    command = command_args[0]

    if command == "Add":
        add(command_args[1], int(command_args[2]), int(command_args[3]))
    elif command == "Message":
        message(command_args[1], command_args[2])
    elif command == "Empty":
        empty(command_args[1])

print(f"Users count: {len(mail_dict)}")
for username in mail_dict:
    print(f"{username} - {sum(mail_dict[username])}")







