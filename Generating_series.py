number_of_terms = int(input("Enter number of terms: "))

current_value = 1
difference = 4
sign = 1

for _ in range(number_of_terms):
    print(current_value * sign, end=" ")
    current_value += difference
    sign *= -1
