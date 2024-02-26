# В матрице найти максимальный положительный элемент, кратный 4.

import random


def max_positive_multiple_of_4(matrix):
    max_num = None

    for row in matrix:
        for num in row:
            if num > 0 and num % 4 == 0:
                if max_num is None or num > max_num:
                    max_num = num

    return max_num


n0, n1 = random.randint(2, 6), random.randint(2, 6)
matrix = [[random.randint(0, 100) for el in range(n0)]for row in range(n1)]
print("Матрица:")
[print(i) for i in matrix]
result = max_positive_multiple_of_4(matrix)

if result is not None:
    print(f"Максимальный положительный элемент, кратный 4: {result}")
else:
    print("В матрице нет положительных элементов, кратных 4")
