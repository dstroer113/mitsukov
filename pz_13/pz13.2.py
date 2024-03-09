# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
import random

def process_matrix(matrix):
    size = len(matrix)
    fmatrix = ([[(matrix[i][j]) * 2 if i != j else matrix[i][j] for j in range(size)] for i in range(size)])
    return fmatrix


n = random.randint(2, 3)
print("Матрица:")
matrix = [[random.randint(0, 10) for el in range(n)]for row in range(n)]
for row in matrix:
    print(row)

result = process_matrix(matrix)

print("Измененная матрица:")
for row in result:
    print(row)
