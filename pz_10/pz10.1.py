# Список игрушек

sp = ['самолет', 'мишка', 'конструктор', 'мяч', 'кораблик']

# Запрос на количество детских садов
n = int(input('Введите количество детских садов n='))

# Создает список игрушек для каждого детского сада
a = [set() for _ in range(n)]

# Ввод игрушек для каждого детского сада
for i in range(n):
    print(f'Выберите игрушки которые есть в детском саду {i+1}')
    print('1-самолет 2-мишка 3-конструктор 4-мяч 5-кораблик 6-выход')
    while True:
        k = int(input())
        if 1 <= k <= 5:
            a[i].add(k)
        elif k == 6:
            break

# Показывает какие игрушки есть в каждом детском саду
print('Наличие игрушек в детских садах')
for i in range(n):
    print(f'№{i+1}: ', end='')
    for j in range(1, 6):
        if j in a[i]:
            print(sp[j-1], end=' ')
    print()

# Находит игрушки которые есть в каждом детском саду
m = set(range(1, 7))
for toys in a:
    m.intersection_update(toys)

print('Игрушки, которые есть во всех садах')
if not m:
    print('Таких игрушек нет')
else:
    for i in m:
        print(sp[i-1], end=' ')
    print()

# Находит игрушки которых нет ни в одном саду
m = set()
for j in range(1, 6):
    if all(j not in toys for toys in a):
        m.add(j)

print('Игрушки которых нет ни в одном саду')
if not m:
    print('Таких игрушек нет')
else:
    for j in m:
        print(sp[j-1], end=' ')