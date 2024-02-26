# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной последовательности из целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Содержимое первого файла:
# Четные элементы:
# Произведение четных элементов:
# Минимальный элемент:
# Содержимое второго файла:
# Нечетные элементы:
# Количество нечетных элементов:
# Сумма нечетных элементов:
import random
import functools
# Задаем списки
positive = []
negative = []
even = []
odd = []
numbers = [random.randint(-100, 100) for i in range(10)]
# Создаем списки положительных и отрицательных чисел и записываем их в файл
for i in range(0, 10):
    if numbers[i] < 0:
        negative = negative + [numbers[i]]
    else:
        positive = positive + [numbers[i]]
with open('base.txt', 'w') as f:
    f.write(f'Положительные числа: {"".join(str(positive))}\n')
    f.write(f'Отрицательные числа: {"".join(str(negative))}')
# Создаем списки четных и нечетных чисел
for i in range(0, 10):
    if numbers[i] % 2 == 0:
        even = even + [numbers[i]]
    else:
        odd = odd + [numbers[i]]
# Записываем в файлы числа по заданию
with open('first.txt', 'w') as frst:
    frst.write(f'Четные числа: {"".join(str(even))}\n')
    frst.write(f'Произведение четных чисел: {"".join(str(functools.reduce(lambda a, b : a * b, even) ))}\n')
    frst.write(f'Минимальное четное число: {"".join(str(min(even)))}\n')
with open('second.txt', 'w') as scnd:
    scnd.write(f'Нечетные числа: {"".join(str(odd))}\n')
    scnd.write(f'Количество нечетных чисел: {"".join(str(len(odd)))}\n')
    scnd.write(f'Сумма нечетных чисел: {"".join(str(functools.reduce(lambda a, b : a + b, odd) ))}\n')
