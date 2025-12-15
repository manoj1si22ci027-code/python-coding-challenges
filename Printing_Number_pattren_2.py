number_of_rows = int(input("Enter number of rows: "))
number_of_columns = int(input("Enter number of columns: "))

for _ in range(number_of_rows):
    for number in range(1, number_of_columns + 1):
        print(number, end="")
    print()
