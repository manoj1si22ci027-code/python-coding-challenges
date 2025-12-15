number_of_rows = int(input("Enter number of rows: "))

for row in range(1, number_of_rows + 1):
    for _ in range(row):
        print(row, end="")
    print()
