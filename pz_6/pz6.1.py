# Дан целочисленный список размера N, не содержащий одинаковых чисел.
# Проверить, образуют ли его элементы арифметическую прогрессию. Если образуют,
# то вывести разность прогрессии, если нет
# вывести 0.
# Ввод размера списка
n = int(input("Введите размер списка: "))
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")
# Ввод элементов списка
print('Введите элементы списка: ')
arr = []
for i in range(n):
    arr.append(int(input()))
# Поиск разности прогрессии и проверка образуют ли числа последовательность
d = arr[1] - arr[0]
i = 1
flag = True
while flag and (i < n):
    if arr[i] - arr[i-1] != d:
        flag = False
        break
    i += 1
# Вывод результата
print(d if flag else 0)