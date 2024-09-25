import random

MATRIX_ROWS = 9
MATRIX_COLUMNS = 4

numbers = [i for i in range(1, MATRIX_ROWS * MATRIX_COLUMNS + 1)]
matrix = []

random.shuffle(numbers)

print(numbers)

for row in range(MATRIX_ROWS):
    matrix.append([])
    for column in range(MATRIX_COLUMNS):
        matrix[row].append(numbers[row + column])

for m in range(len(matrix)):
    print(matrix[m])
