number_of_elements = int(input("Enter number of elements: "))

elements_array = []

even_count = 0
odd_count = 0

for _ in range(number_of_elements):
    value = int(input("Enter element: "))
    elements_array.append(value)

    if value % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Numbers Count:", even_count)
print("Odd Numbers Count:", odd_count)
