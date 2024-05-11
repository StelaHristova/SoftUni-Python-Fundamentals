def add(username, sent, received):
    mail_dict = {}

    if username not in mail_dict:
        mail_dict[username] = [sent, received]
    return mail_dict


def message(mail_dict, sender, receiver):
    if sender in mail_dict and receiver in mail_dict:
        mail_dict[sender][sent] += 1
        mail_dict[receiver][received] += 1
    if mail_dict[sender][sent] + mail_dict[sender][received] >= capacity_of_possible_messages:
        print(f"{mail_dict[sender]} reached the capacity!")
        del mail_dict[sender]
    if mail_dict[receiver][sent] + mail_dict[receiver][received] >= capacity_of_possible_messages:
        print(f"{mail_dict[receiver]} reached the capacity!")
        del mail_dict[receiver]


def empty(mail_dict, username):
    if username in mail_dict:
        del mail_dict[username][sent]
        del mail_dict[username][received]


capacity_of_possible_messages = int(input())

while True:
    line = input()
    if line == "Statistics":
        break

    command_args = line.split("=")
    command = command_args[0]

    if command == "Add":
        username = command_args[1]
        sent = int(command_args[2])
        received = int(command_args[3])

        capacity_of_possible_messages -= sent + received

        if capacity_of_possible_messages <= 0:
            print(f"{username} reached the capacity!")
        else:
            add(username, sent, received)
            print(add(username, sent, received))
    elif command == "Message":
        sender = command_args[1]
        receiver = command_args[2]
        message(mail_dict, sender, receiver)
    elif command == "Empty":
        username = command_args[1]
        if username == "All":
            for user in username:
                del mail_dict[username][sent]
                del mail_dict[username][received]
        else:
            empty(mail_dict, username)

print(f"Users count: {len(mail_dict[username])})
for user in mail_dict:
    print(f"{mail_dict[username]} - {mail_dict[username][sent] + mail_dict[username][received]}")
