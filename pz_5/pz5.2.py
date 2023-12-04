import math


def TrianglePS(a):
    P, S = (3 * a), (a**2 * math.sqrt(3/4))
    print("периметр:",P, "площадь:",S)


a, b, c = input("Сторона первого треугольника:"), input("Сторона второго треугольника:"), input("Сторона третьего треугольника:")

while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите число: ")
while type(b) != float:
    try:
        b = float(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите число: ")
while type(c) != float:
    try:
        c = float(c)
    except ValueError:
        print("Неправильно ввели!")
        c = input("Введите число: ")

print("Первый треугольник:"), TrianglePS(a), print("Второй треугольник:"), TrianglePS(b),print("Третий треугольник:"), TrianglePS(c)
