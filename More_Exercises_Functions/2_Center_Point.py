from math import floor
def closest(x1, y1, x2, y2):
    first_sum = abs(x1) + abs(y1)
    second_sum = abs(x2) + abs(y2)
    if first_sum <= second_sum:
        print(f"{floor(x1), floor(y1)}")
    else:
        print(f"{floor(x2), floor(y2)}")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

closest(x1, y1, x2, y2)