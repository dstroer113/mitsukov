# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
import random

def increase_elements(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] *= 2

    return matrix


n = random.randint(2, 6)
print("Матрица:")
matrix = [[random.randint(0, 100) for el in range(n)]for row in range(n)]
for row in matrix:
    print(row)

result = increase_elements(matrix)

print("Измененная матрица:")
for row in result:
    print(row)
