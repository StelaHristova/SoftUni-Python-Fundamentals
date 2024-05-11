def one_is_full(n1):
    n1 -= max_number_of_electrons_in_shell
    return n1


def all_is_full(n2):
    return 0


number_of_electrons = int(input())
list_of_shells = []
counter = 0

while number_of_electrons > 0:
    counter += 1
    max_number_of_electrons_in_shell = 2 * (counter ** 2)

    if max_number_of_electrons_in_shell <= number_of_electrons:
        number_of_electrons = one_is_full(number_of_electrons)
        list_of_shells.append(max_number_of_electrons_in_shell)
    else:
        list_of_shells.append(number_of_electrons)
        number_of_electrons = all_is_full(number_of_electrons)

print(list_of_shells)
