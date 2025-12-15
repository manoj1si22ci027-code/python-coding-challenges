number_of_rows = int(input("Enter number of rows: "))

first_number = 1
second_number = 1

for row in range(1, number_of_rows + 1):
    for _ in range(row):
        print(first_number, end=" ")
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number
    print()
