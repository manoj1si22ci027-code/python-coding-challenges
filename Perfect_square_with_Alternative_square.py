number_of_rows = int(input("Enter number of rows: "))

current_number = 1
sign = 1

for row in range(1, number_of_rows + 1):
    for _ in range(row):
        square_value = current_number * current_number * sign
        print(square_value, end=" ")
        sign *= -1
        current_number += 1
    print()
