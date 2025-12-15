import numpy as np

number_of_rows = int(input("Enter number of rows: "))
number_of_columns = int(input("Enter number of columns: "))

matrix = np.zeros((number_of_rows, number_of_columns), dtype=int)

for row_index in range(number_of_rows):
    for column_index in range(number_of_columns):
        matrix[row_index][column_index] = int(input("Enter element: "))

search_element = int(input("Enter element to search: "))

element_found = False

for row_index in range(number_of_rows):
    for column_index in range(number_of_columns):
        if matrix[row_index][column_index] == search_element:
            element_found = True
            break
    if element_found:
        break

if element_found:
    print("Element Found")
else:
    print("Element Not Found")
