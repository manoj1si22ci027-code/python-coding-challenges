number_of_terms = int(input("Enter number of terms: "))

current_value = 1
difference = 1

for _ in range(number_of_terms):
    print(current_value, end=" ")
    current_value += difference
    difference += 1
