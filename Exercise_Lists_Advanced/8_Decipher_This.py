def decipher(number):
    if 97 <= ord(number.lower()) <= 122:
        return str(number)
    else:
        return int(number)


secret_message = input().split()

for a in range(len(secret_message)):
    current_message = [i for i in secret_message[a]]

    for word in range(len(current_message)):
        current_message[word] = decipher(current_message[word])

    number = ""

    for digit in range(len(current_message)):
        if 97 <= ord(str(current_message[digit]).lower()) <= 122:
            break
        else:
            number += str(current_message[digit])

    current_message = [i for i in current_message if i == str(i)]
    current_message.insert(0, chr(int(number)))
    current_message[1], current_message[-1] = current_message[-1], current_message[1]

    print("".join(current_message), end=" ")