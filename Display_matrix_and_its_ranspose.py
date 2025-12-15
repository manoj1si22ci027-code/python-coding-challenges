import numpy as np

number_of_rows = int(input())
number_of_columns = int(input())

matrix = np.zeros((number_of_rows, number_of_columns), dtype=int)

for row_index in range(number_of_rows):
    for column_index in range(number_of_columns):
        matrix[row_index][column_index] = int(input())

transpose_matrix = np.zeros((number_of_columns, number_of_rows), dtype=int)

for row_index in range(number_of_rows):
    for column_index in range(number_of_columns):
        transpose_matrix[column_index][row_index] = matrix[row_index][column_index]

print("Original Matrix:")
print(matrix)

print("Transpose Matrix:")
print(transpose_matrix)
