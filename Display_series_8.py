number_of_terms = int(input("Enter number of terms: "))

first_number = 1
second_number = 1

for _ in range(number_of_terms):
    print(first_number, end=" ")
    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number
