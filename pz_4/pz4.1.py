# Даны целые положительные числа N и К. Найти сумму 1^К + 2^К + N^K.
# ввод числа
n, k = input('Конечное число '), input('Cтепень ')
# обработка исключений
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите число: ")
while type(k) != int:
    try:
        k = int(k)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите число: ")
while n < 0 or k < 0 :
    print("Введенные числа не положительные!")
    n, k = int(input('Конечное число ')), int(input('Cтепень '))
# работа с числом
res = 0
for i in range(1, n+1):
    res = res+i**k
# результат
print(res)