def collect(list, item_input):
    if item_input not in list:
        list.append(item_input)
    return list


def drop(list, item_input):
    if item_input in list:
        list.remove(item_input)
    return list


def renew(list, item_input):
    if item_input in list:
        list.remove(item_input)
        list.append(item_input)
    return list


journal = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")
    action = command[0]

    if action == "Collect":
        item = command[1]
        journal = collect(journal, item)
    elif action == "Drop":
        item = command[1]
        journal = drop(journal, item)
    elif action == "Combine Items":
        current_command = command[1].split(":")
        for i in range(len(journal) - 1, - 1, - 1):
            if current_command[0] == journal[i]:
                journal.insert(i + 1, current_command[1])
    elif action == "Renew":
        item = command[1]
        journal = renew(journal, item)

    command = input()

print(", ".join(journal))