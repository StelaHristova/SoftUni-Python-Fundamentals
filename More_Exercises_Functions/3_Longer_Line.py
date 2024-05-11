from math import floor
def closest(x_1, y_1, x_2, y_2):
    return (x_2 - x_1) ** 2 + (y_2 - y_1) ** 2


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

x1y1 = closest(x1, y1, 0, 0)
x2y2 = closest(x2, y2, 0, 0)
x3y3 = closest(x3, y3, 0, 0)
x4y4 = closest(x4, y4, 0, 0)

first_line = x1y1 + x2y2
second_line = x3y3 + x4y4

if first_line >= second_line:
    if x1y1 <= x2y2:
        print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})({floor(x2)}, {floor(y2)})")
else:
    if x3y3 <= x4y4:
        print(f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})")
    else:
        print(f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})")