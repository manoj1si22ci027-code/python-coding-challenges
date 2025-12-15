number_of_rows = int(input("Enter number of rows: "))
number_of_columns = int(input("Enter number of columns: "))

for _ in range(number_of_rows):
    for _ in range(number_of_columns):
        print("*", end="")
    print()
