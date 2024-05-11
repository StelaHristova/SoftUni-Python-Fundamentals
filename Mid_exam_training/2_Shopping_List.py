products = input().split("!")

while True:
    line = input()

    if line == "Go Shopping!":
        break

    command_arg = line.split()
    command = command_arg[0]
    product = command_arg[1]

    if command == "Urgent":
        if product not in products:
            products.insert(0, product)
    elif command == "Unnecessary":
        if product in products:
            products.remove(product)
    elif command == "Correct":
        new_product = command_arg[2]
        if product in products:
            index = products.index(product)
            products[index] = new_product
    elif command == "Rearrange":
        if product in products:
            products.remove(product)
            products.append(product)

print(", ".join(products))
