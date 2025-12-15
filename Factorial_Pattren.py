number_of_rows = int(input("Enter number of rows: "))

factorial_value = 1
current_number = 1

for row in range(1, number_of_rows + 1):
    for _ in range(row):
        factorial_value *= current_number
        print(factorial_value, end=" ")
        current_number += 1
    print()
