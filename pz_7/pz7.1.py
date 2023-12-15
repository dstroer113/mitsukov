# Дана строка, изображающая арифметическое выражение вида  «<цифра>+<цифра>±...±<цифра>»,
# где на месте знака операции «±» находится символ «+» или «-» (например, «4+7-2-8»).
# Вывести значение данного выражения (целое число).

import string
import numpy
# Ввод количества цифр в примере
n = int(input("Введите количество цифр в выражении :"))
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")
# Функция возвращающая строку с числовым примером (случайные цифры и случайны знак либо + либо -)

def rndmdigits():
    lst_digit = list(numpy.random.choice(list(string.digits), n))
    lst_oper = list(numpy.random.choice(['+','-'], n-1))
    result = [None]*(2*n - 1)
    result[::2] = lst_digit
    result[1::2] = lst_oper
    return "".join(result)
# Использование функции и счет значения выражения с помощью функции eval
s = rndmdigits()
print(s, "=", eval(s))
