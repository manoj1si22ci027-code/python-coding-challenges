
import numpy as np

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = np.zeros((rows, columns), dtype=int)

for row_index in range(rows):
    for column_index in range(columns):
        matrix[row_index][column_index] = int(input("Enter value: "))

print(matrix)
