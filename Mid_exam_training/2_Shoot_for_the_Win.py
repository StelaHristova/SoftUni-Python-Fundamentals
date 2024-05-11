def print_result(targets, shots_counter):
    print(f"Shot targets: {shots_counter} -> {' '.join(str(i) for i in targets)}")


def shot_on_target(targets, index, counter_shots):
    if targets[index] != -1:
        needed_shots = targets[index]
        counter_shots += 1
        targets[index] = -1
        for i in range(len(targets)):
            if targets[i] <= needed_shots and targets[i] != -1:
                targets[i] += needed_shots
            elif targets[i] > needed_shots and targets[i] != -1:
                targets[i] -= needed_shots
    return targets, counter_shots


def targets_to_shot(targets):
    counter = 0
    while True:
        index_of_target = input()
        if index_of_target == "End":
            print_result(targets, counter)
            break

        index_of_target = int(index_of_target)

        if 0 <= index_of_target < len(targets):
            targets, counter = shot_on_target(targets, index_of_target, counter)
        else:
            continue


targets_list = [int(x) for x in input().split(" ")]
targets_to_shot(targets_list)

