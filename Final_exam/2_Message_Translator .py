import re
n = int(input())
data = [input() for _ in range(n)]

pattern = r"\!(?P<name>[A-Z][a-z]{1,})\!\:\[(?P<num>[A-Za-z)]{8,})\]"

for text in data:
    match = re.search(pattern, text)
    if match:
        found_message = []
        for letter in match.group('num'):
            item = ord(letter)
            found_message.append(str(item))
        print(f"{match.group('name')}: {' '.join(found_message)}")
    else:
        print("The message is invalid")


