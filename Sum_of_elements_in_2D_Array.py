import numpy as np

number_of_rows = int(input())
number_of_columns = int(input())

matrix_sum = 0
matrix = np.zeros((number_of_rows, number_of_columns), dtype=int)

for row_index in range(number_of_rows):
    for column_index in range(number_of_columns):
        matrix[row_index][column_index] = int(input())
        matrix_sum += matrix[row_index][column_index]

print(matrix_sum)
