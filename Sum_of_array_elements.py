number_of_elements = int(input("Enter number of elements: "))

elements_array = []
total_sum = 0

for _ in range(number_of_elements):
    value = int(input("Enter element: "))
    elements_array.append(value)
    total_sum += value

print("Sum of Elements:", total_sum)
