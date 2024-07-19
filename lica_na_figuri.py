import math

figure = input().lower()

if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
elif figure == "circle":
    r = float(input())
    area = math.pi * math.pow(r, 2)
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2

print(f'{area:.3f}')
