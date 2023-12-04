n = int(input("Введите размер массива: "))
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")
print('Введите элементы массива: ')
arr = []
for i in range(n):
    arr.append(int(input()))
d = arr[1] - arr[0]
i = 1
flag = True
while flag and (i < n):
    if arr[i] - arr[i-1] != d:
        flag = False
        break
    i += 1
print(d if flag else 0)