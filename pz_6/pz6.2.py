# Дан список А размера N. Сформировать новый список В того же размера, элементы которого определяются следующим образом:
# Вк = 2*Ак, если Ак < 5,
# Ак/2 в противном случае.
# Ввод размера
n = int(input("Введите размер списка: "))
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")
# Ввод элементов списка a
print('Введите элементы списка: ')
a = []
for i in range(n):
    a.append(int(input()))
b = []
print("Список a:\n", a)
# Формирование списка b
for i in range(0, n):
    if a[i] < 5:
        b.append(a[i] * 2)
    else:
        b.append(a[i] / 2)
# Вывод списка b
print("Список b:\n", b)