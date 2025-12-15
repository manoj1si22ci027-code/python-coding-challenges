number_of_terms = int(input("Enter number of terms: "))

current_number = 1
for _ in range(number_of_terms):
    print(current_number, end=" ")
    current_number += 2
