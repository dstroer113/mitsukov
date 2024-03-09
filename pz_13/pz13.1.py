# В матрице найти максимальный положительный элемент, кратный 4.
from itertools import chain
import random

n0, n1 = random.randint(2, 6), random.randint(2, 6)
matrix = [[random.randint(0, 12) for el in range(n0)]for row in range(n1)]
print("Матрица:")
[print(i) for i in matrix]

fmatrix = list(chain.from_iterable(matrix))
max_num = max(filter(lambda x: x%4 == 0 and x > 0, fmatrix))
if max_num is not None:
    print(f"Максимальный положительный элемент, кратный 4: {max_num}")
else:
    print("В матрице нет положительных элементов, кратных 4")
