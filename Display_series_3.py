number_of_terms = int(input("Enter number of terms: "))

current_even = 2
for _ in range(number_of_terms):
    print(current_even * current_even, end=" ")
    current_even += 2
