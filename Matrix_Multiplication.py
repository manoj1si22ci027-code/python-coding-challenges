import numpy as np

rows_matrix_a = int(input())
columns_matrix_a = int(input())

rows_matrix_b = int(input())
columns_matrix_b = int(input())

if columns_matrix_a != rows_matrix_b:
    print("Matrix multiplication not possible")
else:
    matrix_a = np.zeros((rows_matrix_a, columns_matrix_a), dtype=int)
    matrix_b = np.zeros((rows_matrix_b, columns_matrix_b), dtype=int)
    result_matrix = np.zeros((rows_matrix_a, columns_matrix_b), dtype=int)

    for row_index in range(rows_matrix_a):
        for column_index in range(columns_matrix_a):
            matrix_a[row_index][column_index] = int(input())

    for row_index in range(rows_matrix_b):
        for column_index in range(columns_matrix_b):
            matrix_b[row_index][column_index] = int(input())

    for row_index in range(rows_matrix_a):
        for column_index in range(columns_matrix_b):
            for k in range(columns_matrix_a):
                result_matrix[row_index][column_index] += (
                    matrix_a[row_index][k] * matrix_b[k][column_index]
                )

    print("Resultant Matrix:")
    print(result_matrix)
