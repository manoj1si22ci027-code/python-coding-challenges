number_of_rows = int(input("Enter number of rows: "))
number_of_columns = int(input("Enter number of columns: "))

for row in range(1, number_of_rows + 1):
    for _ in range(number_of_columns):
        print(row, end="")
    print()
